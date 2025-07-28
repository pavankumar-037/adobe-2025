
# 🧠 Adobe India Hackathon 2025 – Smart Document Intelligence

This repository contains our submission for the **Adobe India Hackathon 2025**, solving both **Round 1A** and **Round 1B** challenges under the theme:

> **"Connect What Matters – For the User Who Matters"**

--------------------------------------------------------------------------

## 🚀 Overview

We developed two intelligent systems:

### 🔹 Round 1A – Document Structure Extraction
Extracts the document **title** and a structured **outline of headings (H1, H2, H3)** from a variety of PDF documents, using heuristic-based layout parsing and PDF metadata.

### 🔹 Round 1B – Persona-Driven Document Intelligence
Given:
- A set of PDFs
- A **persona** (e.g., researcher, analyst, student)
- A **job-to-be-done** (e.g., literature review, business insight, exam prep)

We extract and **rank the most relevant document sections** based on semantic similarity, using compact sentence-transformers. Output is generated in a structured JSON format.

-------------------------------------------------------------------------------

## 📁 Folder Structure

adobe-hackathon-2025/
├── Round1A_solution/
│ ├── main.py
│ ├── extract_outline.py
│ ├── schema.json
│ ├── requirements.txt
│ ├── Dockerfile
│ └── app/
│ ├── input/
│ └── output/
├── Round1B_solution/
│ ├── main.py
│ ├── pdf_utils.py
│ ├── semantic_ranker.py
│ ├── output_builder.py
│ ├── approach_explanation.md
│ ├── requirements.txt
│ ├── Dockerfile
│ └── Collection1/Collection2/Collection3/
├── README.md

-----------------------------------------------------------------------

## 🧠 Round 1A – Outline Extraction

### ✅ Features:
- Extracts title from PDF metadata or first page.
- Extracts headings (H1, H2, H3) with page numbers based on font size and position.
- JSON output matching given schema.

### 📦 Requirements
```txt
pdfplumber
python-docx
pdfminer.six
PyPDF2
pypdfium2
📄 Example Output
json

{
  "title": "Graph Neural Networks in Drug Discovery",
  "outline": [
    { "level": "H1", "text": "Introduction", "page": 1 },
    { "level": "H2", "text": "Methodology", "page": 3 },
    ...
  ]
}
🧠 Round 1B – Persona-Driven Section Ranking
✅ Features:
Parses PDFs page by page using PyMuPDF.

Uses sentence-transformers for embedding.

Computes cosine similarity between each chunk and the persona+job query.

Ranks sections and sub-sections by relevance.

Outputs results in challenge1b_generated_output.json.

📦 Requirements:

sentence-transformers==2.2.2
torch==2.0.0
transformers==4.28.1
PyMuPDF==1.23.9
numpy==1.23.5
scikit-learn==1.2.2
scipy==1.10.1
pandas==1.5.3
🛠 Output Format
json

{
  "metadata": {
    "documents": ["doc1.pdf", "doc2.pdf"],
    "persona": "...",
    "job": "...",
    "timestamp": "..."
  },
  "section_analysis": [
    {
      "document": "doc1.pdf",
      "page_number": 4,
      "section_title": "Transformer Architecture",
      "importance_rank": 1
    },
    ...
  ],
  "subsection_analysis": [
    {
      "document": "doc1.pdf",
      "page_number": 4,
      "refined_text": "...",
      "importance_rank": 1
    }
  ]
}
🐳 Docker Instructions
🧱 Build Docker Image

docker build -t adobe-r1a ./Round1A_solution
docker build -t adobe-r1b ./Round1B_solution
▶️ Run Container
Round 1A
docker run --rm -v ${PWD}/Round1A_solution/app:/app/app adobe-r1a
Round 1B
docker run --rm -v ${PWD}/Round1B_solution:/app adobe-r1b
📑 Submissions
🔹 Round 1A Submission
GitHub: 🔗 Link to Round 1A

ZIP Upload: Round1A_submission.zip

🔹 Round 1B Submission
GitHub: 🔗 Link to Round 1B

ZIP Upload: Round1B_submission.zip

👨‍💻 Author & Contact
Pavan Kumar
Adobe India Hackathon 2025 Participant
✉️ Reach out via GitHub or Unstop DM

✅ License
This repository is submitted as part of the Adobe India Hackathon 2025 and is intended for educational/demo purposes only.

