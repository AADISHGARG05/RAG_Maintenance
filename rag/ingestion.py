import os
import pdfplumber
from langchain_text_splitters import RecursiveCharacterTextSplitter
def load_pdfs(data_dir="data"):
    documents = []
    for file in os.listdir(data_dir):
        if not file.lower().endswith(".pdf"):
            continue

        file_path = os.path.join(data_dir, file)

        with pdfplumber.open(file_path) as pdf:
            for page_num, page in enumerate(pdf.pages, start=1):
                text = page.extract_text()
                if not text or not text.strip():
                    continue

                documents.append({
                    "text": text.strip(),
                    "metadata": {
                        "source": file,
                        "page": page_num,
                        "doc_id": file
                    }
                })

    print(f"Loaded {len(documents)} pages")
    return documents


def chunk_documents(documents):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=400,
        chunk_overlap=80,
        separators=["\n\n", "\n", ".", " "]
    )

    chunks = []

    for doc in documents:
        for i, chunk in enumerate(splitter.split_text(doc["text"])):
            if len(chunk.strip()) < 50:
                continue

            chunks.append({
                "text": chunk,
                "metadata": {
                    **doc["metadata"],
                    "chunk_id": i
                }
            })

    print(f"Created {len(chunks)} chunks")
    return chunks
