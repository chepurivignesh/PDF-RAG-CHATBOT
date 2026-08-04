import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

from dotenv import load_dotenv
load_dotenv()

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import (
    GoogleGenerativeAIEmbeddings,
    ChatGoogleGenerativeAI,
)
from langchain_community.vectorstores import InMemoryVectorStore

import streamlit as st
from time import sleep
##LLM  
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

## Session State 
if "vector_db" not in st.session_state:
    st.session_state.vector_db = None

if "document_uploaded" not in st.session_state:
    st.session_state.document_uploaded = False


## Document Processing
def document_process(path):
    try:
        # Load PDF
        loader = PyPDFLoader(path)
        docs = loader.load()

        # Split into chunks
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=3500,
            chunk_overlap=150
        )

        docs = text_splitter.split_documents(docs)

        st.info(f"📄 Total Chunks Created: {len(docs)}")

        # Embeddings
        embeddings = GoogleGenerativeAIEmbeddings(
            model="gemini-embedding-2-preview"
        )

        # Vector Store
        vector_db = InMemoryVectorStore.from_documents(
            documents=docs,
            embedding=embeddings
        )

        st.session_state.vector_db = vector_db
        st.session_state.document_uploaded = True

    except Exception as e:
        st.error(f"Document Processing Failed:\n\n{e}")


## UI
st.title("📄 Document Chatbot")

st.subheader("Ask Questions From Your PDF")

##Upload 
if not st.session_state.document_uploaded:

    file = st.file_uploader(
        "Upload a PDF File",
        type=["pdf"]
    )

    if file:

        with open("uploaded_document.pdf", "wb") as f:
            f.write(file.getvalue())

        with st.spinner("Processing Document..."):

            document_process("uploaded_document.pdf")

        if st.session_state.document_uploaded:
            st.success("✅ Document Processed Successfully!")

            sleep(1.5)

            st.rerun()

## chat
if (
    st.session_state.document_uploaded
    and st.session_state.vector_db is not None
):

    query = st.text_input("Ask a Question")

    if query:

        st.chat_message("user").markdown(query)

        try:

            documents = st.session_state.vector_db.similarity_search(
                query,
                k=6
            )

            context = ""

            pages = sorted(
                set(doc.metadata["page"] + 1 for doc in documents)
            )

            for doc in documents:

                page = doc.metadata["page"] + 1

                context += (
                    f"Page {page}:\n"
                    f"{doc.page_content}\n\n"
                )

            prompt = f"""
You are a helpful document assistant.

Answer ONLY using the provided context.

If the answer is not present in the context,
reply exactly:

"I could not find that information in the document."

Context:
{context}

Question:
{query}

Answer:
"""

            result = llm.invoke(prompt)

            if isinstance(result.content, list):

                answer = "\n".join(
                    block["text"]
                    for block in result.content
                    if block.get("type") == "text"
                )

            else:

                answer = result.content

            st.chat_message("assistant").markdown(answer)

            st.caption(
                f"📄 Source Pages: {', '.join(map(str, pages))}"
            )

        except Exception as e:

            st.error(f"Error while generating answer:\n\n{e}")

##Upload Another pdf
if st.session_state.document_uploaded:

    if st.button("📂 Upload Another Document"):

        st.session_state.vector_db = None
        st.session_state.document_uploaded = False

        st.rerun()