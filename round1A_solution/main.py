import os
import json
from extract_outline import extract_outline

INPUT_DIR = "./app/input"
OUTPUT_DIR = "./app/output"

def main():
    for filename in os.listdir(INPUT_DIR):
        if filename.endswith(".pdf"):
            input_path = os.path.join(INPUT_DIR, filename)
            print(f"[INFO] Processing {filename}...")
            result = extract_outline(input_path)
            output_path = os.path.join(OUTPUT_DIR, filename.replace(".pdf", ".json"))
            with open(output_path, "w", encoding="utf-8") as f:
                json.dump(result, f, indent=2)
            print(f"[SUCCESS] Output saved to {output_path}")

if __name__ == "__main__":
    main()
