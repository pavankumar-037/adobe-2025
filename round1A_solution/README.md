# Adobe Hackathon 2025 – Round 1A: Document Structure Extractor

## 🔍 Challenge Overview

In Round 1A of Adobe's *Connecting the Dots* Hackathon, we were tasked with transforming PDFs into structured, machine-readable outlines. This includes extracting:

- 📘 Title (from metadata or first large heading)
- 🧩 Headings (H1, H2, H3) with page numbers
- 🧾 JSON output matching the Adobe-provided schema

-------------------------------------------------------------------------

## 🚀 Our Approach

We built a **Dockerized Python solution** that:

1. Uses `pdfplumber` to parse text, position, and font size from each page.
2. Collects font size statistics across the document to estimate heading levels.
3. Infers:
   - H1: Most frequent large font
   - H2: Medium font
   - H3: Smaller consistent font
4. Returns a clean, schema-compliant JSON structure.

To ensure robustness, we:
- Skip elements missing font size
- Sort font sizes by frequency, not absolute value
- Avoid relying on TOC or hardcoded keywords

---

## 📦 Dependencies

All dependencies are installed within the Docker container:

pdfplumber
pdfminer.six
PyPDF2
pypdfium2
jsonschema


> These are listed in `requirements.txt`

-------------------------------------------------------------------------

## 🛠️ Build & Run Instructions

### 🧱 Build the Docker Image

```bash
docker build -t round1a-solution .

▶ Run the Container
Make sure your input PDFs are in app/input/, then run:

docker run --rm \
  -v "$(pwd)/app/input:/app/app/input" \
  -v "$(pwd)/app/output:/app/app/output" \
  round1a-solution
PowerShell users on Windows: replace $(pwd) with your full path or use ${PWD}.

 Input/Output Format
✅ Input
All .pdf files placed in /app/input/ inside the container.

✅ Output
For each filename.pdf, a corresponding filename.json is written to /app/output/. The format matches Adobe's schema:

{
  "title": "Understanding AI",
  "outline": [
    { "level": "H1", "text": "Introduction", "page": 1 },
    { "level": "H2", "text": "History of AI", "page": 2 },
    { "level": "H3", "text": "Symbolic AI", "page": 3 }
  ]
}
Schema compliance is enforced via jsonschema before saving.

🔐 Constraints Met
✅ CPU-only (no GPU dependencies)

✅ Model-free (no large weights or downloads)

✅ Works offline (no network access)

✅ Output under 10s for 50-page PDFs (tested)

📁 Project Structure

round1A_solution/
├── app/
│   ├── input/          # Place your input PDFs here
│   └── output/         # Extracted JSONs will be written here
├── Dockerfile
├── main.py
├── extract_outline.py
├── schema.py
├── requirements.txt
└── README.md           

✅ Submission Checklist
 Working Dockerfile

 Self-contained logic (no external API calls)

 JSON output validated against schema

 Fast execution under resource constraints

 README included with instructions

