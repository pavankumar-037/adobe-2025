import pdfplumber
import os
import re

def extract_outline(file_path):
    title = "Untitled Document"
    outline = []

    try:
        with pdfplumber.open(file_path) as pdf:
            for i, page in enumerate(pdf.pages, 1):
                text_objects = page.extract_words(extra_attrs=["size", "fontname"])
                for word in text_objects:
                    try:
                        size = round(float(word.get("size", 0)), 1)
                        text = word.get("text", "").strip()
                        fontname = word.get("fontname", "")

                        if not text or len(text) < 3:
                            continue

                        # Heuristic for heading
                        if size >= 12 and text.isupper():
                            level = "H1"
                        elif 11 <= size < 12:
                            level = "H2"
                        elif 10 <= size < 11:
                            level = "H3"
                        else:
                            continue

                        outline.append({
                            "level": level,
                            "text": text,
                            "page": i
                        })
                    except Exception:
                        continue

        if len(outline) > 0:
            title = outline[0]["text"]

    except Exception as e:
        print(f"[ERROR] Failed to process {file_path}: {e}")

    return {
        "title": title,
        "outline": outline
    }
