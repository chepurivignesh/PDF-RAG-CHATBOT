# 📄 PDF Q&A Chatbot — RAG

An AI-powered PDF Question Answering application that allows users to upload PDF documents and ask questions based on their content.

The application uses **Retrieval-Augmented Generation (RAG)** to retrieve relevant information from the uploaded document and generate context-aware answers using **Google Gemini**.

## 🚀 Features

* 📄 Upload and process PDF documents
* 💬 Ask questions about the uploaded document
* 🔍 Retrieve relevant document content using semantic search
* 🧠 Generate context-aware answers using Google Gemini
* 🔗 Retrieval-Augmented Generation (RAG) pipeline
* ⚡ Interactive question-answering interface

## 🧠 How It Works

The application follows a RAG-based workflow:

```text
PDF Document
     ↓
Document Loading
     ↓
Text Extraction & Chunking
     ↓
Text Embeddings
     ↓
Vector / Semantic Retrieval
     ↓
Relevant Context
     ↓
Google Gemini
     ↓
Generated Answer
```

### 🔍 RAG Pipeline

1. **Document Loading**
   The uploaded PDF is processed and its text content is extracted.

2. **Text Chunking**
   The extracted content is divided into smaller chunks for efficient retrieval.

3. **Embeddings**
   Document chunks are converted into numerical vector representations.

4. **Semantic Retrieval**
   When a user asks a question, relevant document content is retrieved based on semantic similarity.

5. **Answer Generation**
   The retrieved context is provided to Google Gemini to generate a relevant answer.

## 🛠️ Tech Stack

* **Python**
* **LangChain**
* **Google Gemini**
* **Retrieval-Augmented Generation (RAG)**
* **Embeddings**
* **Semantic Search**
* **PDF Processing**

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

> The project structure may vary depending on the current implementation.

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

The application will start locally and provide a URL that you can open in your browser.

## 🔐 Environment Variables

This project uses an environment variable for the Google Gemini API key.

Create a `.env` file:

```env
GOOGLE_API_KEY=your_google_api_key_here
```

**Never commit your actual API key to GitHub.**

## 🎯 Use Case

This project demonstrates how **Retrieval-Augmented Generation (RAG)** can be used to build document-based AI applications that answer questions using information contained within uploaded PDF files.

## 📚 What I Learned

Through this project, I gained practical experience with:

* Building a RAG pipeline
* Document processing and text chunking
* Embeddings and semantic retrieval
* Working with LLMs
* LangChain-based AI application development
* Integrating Google Gemini into an AI application
* Building document question-answering systems

## 🔮 Future Improvements

* Support for multiple PDF documents
* Conversation history and contextual follow-up questions
* Improved document retrieval
* Hybrid search using semantic + keyword retrieval
* Source references for generated answers
* Deployment as a public web application

## 👨‍💻 Author

**Vignesh Chepuri**

* 💼 [LinkedIn](https://www.linkedin.com/in/vignesh-chepuri-5a1399218)
* 🐙 [GitHub](https://github.com/chepurivignesh)

---

⭐ If you find this project interesting, feel free to explore the repository.
