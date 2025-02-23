import pandas as pd
import json
import PyPDF2
from io import StringIO
import csv

def process_file(uploaded_file):
    """Process different file types and extract data."""
    file_type = uploaded_file.type

    if file_type == 'text/csv':
        return process_csv(uploaded_file)
    elif file_type == 'application/json':
        return process_json(uploaded_file)
    elif file_type == 'text/plain':
        return process_txt(uploaded_file)
    elif file_type == 'application/pdf':
        return process_pdf(uploaded_file)
    else:
        raise ValueError(f"Unsupported file type: {file_type}")

def process_csv(file):
    """Process CSV files and return both DataFrame and text content."""
    df = pd.read_csv(file)
    # Convert DataFrame to string for word cloud
    text_content = ' '.join(df.astype(str).values.flatten())
    return {'data': df, 'text': text_content}

def process_json(file):
    """Process JSON files and return both DataFrame and text content."""
    data = json.load(file)
    df = pd.json_normalize(data)
    # Convert to string for word cloud
    text_content = ' '.join(df.astype(str).values.flatten())
    return {'data': df, 'text': text_content}

def process_txt(file):
    """Process text files."""
    content = file.read().decode('utf-8')
    # For text files, create a simple DataFrame with the content
    df = pd.DataFrame({'text': [content]})
    return {'data': df, 'text': content}

def process_pdf(file):
    """Process PDF files."""
    pdf_reader = PyPDF2.PdfReader(file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    # Create DataFrame with extracted text
    df = pd.DataFrame({'text': [text]})
    return {'data': df, 'text': text}