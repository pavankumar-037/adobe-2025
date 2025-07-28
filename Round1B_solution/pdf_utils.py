import os
import fitz  # PyMuPDF

def extract_pages_from_pdfs(pdf_dir):
    chunks = []

    for filename in os.listdir(pdf_dir):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(pdf_dir, filename)

            try:
                doc = fitz.open(pdf_path)
                for page_num, page in enumerate(doc, start=1):
                    text = page.get_text()
                    if text and len(text.strip()) > 100:
                        chunks.append({
                            "source": filename,
                            "page": page_num,
                            "content": text.strip()
                        })
                doc.close()
            except Exception as e:
                print(f"[ERROR] Could not read {filename}: {e}")

    return chunks
