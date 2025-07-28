Adobe India Hackathon 2025 – Round 1B
📄 Persona-Driven Document Intelligence

# Approach Explanation – Round 1B

## 🔍 Problem Summary

In this challenge, the task is to build an intelligent document processing system that analyzes a collection of PDFs and extracts the most relevant sections and subsections based on a given **persona** and their **job-to-be-done**. The system must be generic enough to handle various domains, personas, and tasks — from research papers to corporate reports and educational content.

---

## 🧠 Solution Overview

The solution consists of a Python-based pipeline that works entirely offline, uses CPU-only resources, and produces structured JSON output as per the given schema.

The core idea is to:
1. **Parse PDF documents**
2. **Split content into chunks**
3. **Embed and rank them semantically** against the input query (persona + job)
4. **Generate ranked section and subsection outputs**

---

## 🛠 System Components

### 1. `main.py`
- Acts as the orchestrator.
- Iterates through all `Collection` folders.
- Reads the input persona and job from `challenge1b_input.json`.
- Combines them into a semantic query.
- Invokes processing modules to extract, rank, and write output.

### 2. `pdf_utils.py`
- Uses `PyMuPDF` to parse each page of every PDF in the `PDFs/` folder.
- Creates content chunks tagged with page number and source file.

### 3. `semantic_ranker.py`
- Loads a compact Sentence Transformer model (`paraphrase-MiniLM-L6-v2`).
- Computes sentence embeddings for the query and document chunks.
- Ranks:
  - **Sections**: Pages with highest semantic similarity.
  - **Subsections**: Best-matching passages within top pages.

### 4. `output_builder.py`
- Formats the output into a JSON structure with:
  - Metadata
  - Section analysis
  - Subsection analysis

---

## 💡 Ranking Strategy

- Each page is treated as a candidate "section".
- A similarity score is computed using cosine similarity between the query and page text.
- The top N sections are returned (based on a cutoff or top-k).
- From each top section, we further extract meaningful snippets (e.g., paragraphs or sentences) for **subsection analysis**, and rank them similarly.

---

## ⚙️ Technical Constraints & Compliance

- ✅ Entire solution runs **offline**, with **no internet dependency**.
- ✅ All models and libraries used are **CPU-compatible** and under **1GB**.
- ✅ Execution completes within the **60 seconds limit** for a standard collection.

---

## 📦 Deployment & Usage

- Can be run as a simple Python script with `requirements.txt`.
- Or built and executed in a Docker container using the provided `Dockerfile`.
- Output is saved in each `Collection` folder as `challenge1b_generated_output.json`.

---

## ✅ Generalization

- The use of a semantic embedding model allows flexibility to adapt to:
  - Any type of persona (analyst, student, etc.)
  - Any type of job (summarization, review, insight extraction)
  - Any type of document (research, reports, books)

---

## 🚀 Conclusion

This modular, efficient pipeline serves as a general-purpose intelligent document analyzer, fulfilling the challenge goal of **"Connecting what matters — for the user who matters"**.
