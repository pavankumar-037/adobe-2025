import os
import json
from datetime import datetime
from pdf_utils import extract_pages_from_pdfs
from semantic_ranker import rank_sections, rank_subsections
from output_builder import build_output


BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # where Collection folders are

def main():
    for collection in os.listdir(BASE_DIR):
        collection_path = os.path.join(BASE_DIR, collection)
        if not os.path.isdir(collection_path):
            continue

        print(f"\n📂 Processing: {collection}")
        input_path = os.path.join(collection_path, "challenge1b_input.json")
        pdf_dir = os.path.join(collection_path, "PDFs")
        output_path = os.path.join(collection_path, "challenge1b_generated_output.json")

        if not os.path.exists(input_path) or not os.path.exists(pdf_dir):
            print("❌ Skipping - Missing input.json or PDFs folder.")
            continue

        with open(input_path, "r", encoding="utf-8") as f:
            input_data = json.load(f)

        persona = input_data.get("persona", "")
        job = input_data.get("job", "")
        query = f"{persona}: {job}"

        print(f"👤 Persona: {persona}\n🎯 Job: {job}")

        # Step 1: Extract text chunks
        chunks = extract_pages_from_pdfs(pdf_dir)

        if not chunks:
            print("⚠️ No content extracted.")
            continue

        # Step 2: Rank sections
        top_sections = rank_sections(chunks, query)

        # Step 3: Rank sub-sections (within top-ranked sections)
        top_subsections = rank_subsections(top_sections, query)

        # Step 4: Output
        timestamp = datetime.utcnow().isoformat() + "Z"
        documents = list({c["source"] for c in chunks})
        output = build_output(persona, job, documents, timestamp, top_sections, top_subsections)

        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(output, f, indent=2)

        print(f"✅ Output written to: {output_path}")

if __name__ == "__main__":
    main()
