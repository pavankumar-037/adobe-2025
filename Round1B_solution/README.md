# Adobe India Hackathon 2025 — Round 1B Solution 🧠📄

This project processes multiple PDF collections to extract and rank the most relevant sections based on a given persona and job-to-be-done.

------------------------------------------------------------------------

## 🗂 Folder Structure

Challenge_1b/
├── Collection 1/
│ ├── challenge1b_input.json
│ ├── PDFs/
│ │ ├── file1.pdf
│ │ └── file2.pdf
├── Collection 2/
│ ├── challenge1b_input.json
│ ├── PDFs/
│ └── ...

---------------------------------------------------------------------

Each collection gets a `challenge1b_generated_output.json` after processing.

----------------------------------------------------------------------

## 🛠 Setup Instructions

### 🔹 1. Create and activate virtual environment (Windows PowerShell)

```powershell
python -m venv .venv
. .\.venv\Scripts\Activate
🔹 2. Install dependencies

pip install -r requirements.txt
▶️ How to Run

python main.py
That’s it! The script will automatically:

Loop through each collection folder

Read PDFs

Analyze relevance using sentence-transformers

Output a valid JSON file with:

Metadata

Ranked sections

Ranked sub-sections

💡 Example Output
challenge1b_generated_output.json

{
  "metadata": {
    "persona": "Travel Blogger",
    "job": "Write a travel guide...",
    "documents": ["file1.pdf"],
    "timestamp": "2025-07-27T18:00:00Z"
  },
  "section_analysis": [
    {
      "document": "file1.pdf",
      "page": 2,
      "section_title": "",
      "importance_rank": 1
    }
  ],
  "subsection_analysis": [
    {
      "document": "file1.pdf",
      "page": 2,
      "refined_text": "Provence offers rich history...",
      "importance_rank": 1
    }
  ]
}
🧠 Model Details
Model: paraphrase-MiniLM-L6-v2

Engine: sentence-transformers

Fully CPU-compatible and offline

Total size: ~100MB

📦 Docker Setup (Optional)
Add this Dockerfile:

FROM python:3.10-slim

WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "main.py"]
Build + run:


docker build -t adobe-r1b .
docker run --rm -v ${PWD}:/app adobe-r1b
📧 Questions?
If you’re a hackathon judge or participant with questions, contact me via GitHub or email.

💡 Made for the Adobe India Hackathon 2025 - Round 1B