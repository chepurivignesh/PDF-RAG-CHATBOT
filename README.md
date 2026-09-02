# 📄 PDF Q&A Chatbot — RAG

An AI-powered PDF Question Answering application that allows users to upload a PDF document and ask questions based on its content.

The application uses **Retrieval-Augmented Generation (RAG)** to retrieve relevant information from the uploaded document and generate context-aware answers using **Google Gemini**.

## 🚀 Features

* 📄 Upload a PDF document
* 💬 Ask questions about the uploaded document
* 🔍 Retrieve relevant document content using semantic similarity search
* 🧠 Generate answers using Google Gemini
* 📚 Retrieval-Augmented Generation (RAG) pipeline
* 📄 Display source page numbers for retrieved information
* 🔄 Upload another document without restarting the application
* ⚡ Interactive Streamlit interface

## 🧠 How It Works

The application follows a RAG-based workflow:

```text
📄 PDF Upload
      ↓
PyPDFLoader
      ↓
Text Extraction
      ↓
Recursive Text Chunking
      ↓
Gemini Embeddings
      ↓
In-Memory Vector Store
      ↓
Similarity Search (Top 6)
      ↓
Relevant Context
      ↓
Gemini 2.5 Flash
      ↓
Context-Aware Answer
      ↓
📄 Source Pages
```

### 🔍 RAG Pipeline

1. **PDF Loading**
   The uploaded PDF is loaded using `PyPDFLoader`.

2. **Text Chunking**
   The extracted document content is divided into smaller chunks using `RecursiveCharacterTextSplitter`.

3. **Embeddings**
   The document chunks are converted into vector representations using `gemini-embedding-2-preview`.

4. **Vector Storage**
   The generated embeddings are stored in an `InMemoryVectorStore`.

5. **Similarity Retrieval**
   When a user asks a question, the application retrieves the top 6 relevant document chunks using similarity search.

6. **Answer Generation**
   The retrieved context is passed to `gemini-2.5-flash`, which generates an answer based only on the provided context.

7. **Source Pages**
   The application displays the page numbers associated with the retrieved content.

## 🛠️ Tech Stack

* **Python**
* **Streamlit**
* **LangChain**
* **LangChain Community**
* **Google Gemini**
* **Gemini 2.5 Flash**
* **Gemini Embedding 2 Preview**
* **Retrieval-Augmented Generation (RAG)**
* **In-Memory Vector Store**
* **Semantic Similarity Search**
* **PyPDFLoader**

## 📂 Project Structure

```text
PDF-RAG-CHATBOT/
│
├── app.py
├── requirements.txt
├── .gitignore
├── .env.example
└── README.md
```

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/chepurivignesh/PDF-RAG-CHATBOT.git
```

### 2. Navigate to the project directory

```bash
cd PDF-RAG-CHATBOT
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

Activate it:

**Windows:**

```bash
.venv\Scripts\activate
```

**macOS/Linux:**

```bash
source .venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure your API key

Create a `.env` file in the project root:

```env
GOOGLE_API_KEY=your_google_api_key_here
```

Replace the placeholder with your own Google Gemini API key.

### 6. Run the application

```bash
streamlit run app.py
```

The application will open in your browser.

## 🔐 Environment Variables

This application requires a Google API key for Gemini.

Create a `.env` file:

```env
GOOGLE_API_KEY=your_google_api_key_here
```

**Never commit your actual API key to GitHub.**

## 🎯 Use Case

This project demonstrates how **Retrieval-Augmented Generation (RAG)** can be used to build document-based AI applications that answer questions using information contained within uploaded PDF documents.

## 📚 What I Learned

Through this project, I gained practical experience with:

* Building a RAG pipeline
* PDF document processing
* Text chunking
* Generating and using embeddings
* Semantic similarity search
* Working with Large Language Models
* Integrating Google Gemini with LangChain
* Building AI applications using Streamlit
* Providing source page references with generated answers

## 🔮 Future Improvements

* Support for multiple PDF documents
* Conversation history
* Contextual follow-up questions
* Improved retrieval strategies
* Hybrid search using semantic and keyword retrieval
* Source text citations
* Persistent vector database
* Public deployment

## 👨‍💻 Author

**Vignesh Chepuri**

* 💼 [LinkedIn](https://www.linkedin.com/in/vignesh-chepuri-5a1399218)
* 🐙 [GitHub](https://github.com/chepurivignesh)

---

⭐ Feel free to explore the repository and try the application.
