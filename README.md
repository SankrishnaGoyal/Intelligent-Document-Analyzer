# 🧾 InsightIQ – Intelligent Document Analyzer

**InsightIQ** is an intelligent, multi-format file analysis and Q&A tool powered by **large language models (LLMs)**. Upload files such as **CSV, Excel, PDF, Word, TXT, or even images**, and InsightIQ will automatically extract the content, display previews, and allow you to **ask natural language questions** about the file contents.

It integrates **Streamlit** for the frontend, uses **PyMuPDF**, **python-docx**, **pytesseract**, and **Together.ai’s LLaMA-4-based models** to deliver fast, accurate insights directly from your files.

---

## 🚀 Features

- 📤 **Multi-format support**: Upload `.csv`, `.xlsx`, `.pdf`, `.docx`, `.txt`, `.png`, `.jpg`, and more  
- 🤖 **LLM-powered Q&A**: Ask natural language questions about the content using Meta’s **LLaMA-4-Maverick** model via Together.ai  
- 📊 **Tabular Data Preview**: Display tables, summaries, and data types for structured formats  
- 🧠 **Text Analysis**: Extract and summarize text from documents and images  
- 🔍 **OCR Support**: Extract text from uploaded image files  
- 🌐 **Streamlit-based Web Interface**: Simple, interactive, and user-friendly UI  

---

## 📂 Supported File Types

| Format               | Supported |
|----------------------|-----------|
| CSV (`.csv`)         | ✅        |
| Excel (`.xls`, `.xlsx`) | ✅     |
| PDF (`.pdf`)         | ✅        |
| Word (`.docx`)       | ✅        |
| Text (`.txt`)        | ✅        |
| Images (`.png`, `.jpg`, `.jpeg`) | ✅ |

---

## 🧠 Technologies Used

- `Python 3.x`
- [`Streamlit`](https://streamlit.io/) – Interactive frontend  
- `PyMuPDF (fitz)` – PDF text extraction  
- `python-docx` – DOCX parsing  
- `pytesseract` – OCR for image-based text extraction  
- `Together.ai API` – LLM-based Q&A using Meta’s **LLaMA-4-Maverick-17B**  

---
