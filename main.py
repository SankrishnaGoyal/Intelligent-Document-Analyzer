import streamlit as st
import pandas as pd
import fitz  # PyMuPDF
import docx
import pytesseract
from PIL import Image
import tempfile
import together
import os

# Set your Together API key
os.environ["TOGETHER_API_KEY"] = "b6fe75c51b5468c51422e27cf06fcbd15756665708a32dde9fcd7ee841e3f721"  # Replace this

def parse_uploaded_file(file):
    filename = file.name
    ext = filename.lower().split('.')[-1]

    try:
        if ext == 'csv':
            df = pd.read_csv(file)
            return 'csv', df

        elif ext in ['xls', 'xlsx']:
            df = pd.read_excel(file)
            return 'excel', df

        elif ext == 'txt':
            text = file.read().decode('utf-8')
            return 'text', text

        elif ext == 'docx':
            with tempfile.NamedTemporaryFile(delete=False, suffix=".docx") as tmp:
                tmp.write(file.read())
                tmp_path = tmp.name
            doc = docx.Document(tmp_path)
            text = "\n".join([para.text for para in doc.paragraphs])
            return 'docx', text

        elif ext == 'pdf':
            with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
                tmp.write(file.read())
                tmp_path = tmp.name
            pdf_file = fitz.open(tmp_path)
            text = ""
            for page in pdf_file:
                text += page.get_text()
            return 'pdf', text

        elif ext in ['png', 'jpg', 'jpeg']:
            image = Image.open(file)
            text = pytesseract.image_to_string(image)
            return 'image', text

        else:
            return 'unknown', "Unsupported file type"

    except Exception as e:
        return 'error', f" Error while parsing: {str(e)}"

def query_llm(text, query):
    try:
        together.api_key = os.getenv("TOGETHER_API_KEY")

        prompt = f"You are a data assistant. Here is some context:\n{text}\n\nAnswer this: {query}"

        response = together.Complete.create(
            prompt=prompt,
            model="meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8",
            max_tokens=512,
            temperature=0.7,
            top_p=0.9
        )

        return response["output"]["choices"][0]["text"]

    except Exception as e:
        return f" API Error: {str(e)}"

def main():
    st.set_page_config(page_title="Data Analyst Agent", layout="wide")
    st.title("Data Analyst Agent")

    uploaded_file = st.file_uploader("Upload a file (.csv, .xlsx, .pdf, .docx, .txt, .png, etc.)")

    if uploaded_file:
        file_type, content = parse_uploaded_file(uploaded_file)
        st.success(f"File type detected: {file_type}")

        if isinstance(content, pd.DataFrame):
            st.subheader("Preview of Data")
            st.dataframe(content.head())

            if st.checkbox("Show Summary Statistics"):
                st.write(content.describe())

            if st.checkbox("Show Data Types"):
                st.write(content.dtypes)

        else:
            st.subheader("Extracted Text")
            st.text_area("Content", content[:1000], height=300)

        query = st.text_input(" Ask a question about the uploaded content:")
        if query:
            with st.spinner("Thinking..."):
                response = query_llm(content if isinstance(content, str) else content.to_string(), query)
            st.markdown(f"**Answer:** {response}")

if __name__ == '__main__':
    main()
