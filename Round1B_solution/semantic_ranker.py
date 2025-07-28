from sentence_transformers import SentenceTransformer, util

# Load once globally (fast)
model = SentenceTransformer("paraphrase-MiniLM-L6-v2")


def rank_sections(chunks, query, top_k=10):
    texts = [chunk["content"] for chunk in chunks]
    query_emb = model.encode(query, convert_to_tensor=True)
    doc_embs = model.encode(texts, convert_to_tensor=True)

    similarities = util.cos_sim(query_emb, doc_embs)[0]
    top_indices = similarities.argsort(descending=True)[:top_k]

    top_sections = []
    for rank, idx in enumerate(top_indices, start=1):
        section = chunks[idx]
        section["importance_rank"] = rank
        top_sections.append(section)

    return top_sections


def rank_subsections(sections, query, max_per_section=2):
    subsections = []

    for section in sections:
        lines = section["content"].split("\n")
        # Remove short lines
        lines = [line.strip() for line in lines if len(line.strip()) > 40]

        if not lines:
            continue

        query_emb = model.encode(query, convert_to_tensor=True)
        line_embs = model.encode(lines, convert_to_tensor=True)

        similarities = util.cos_sim(query_emb, line_embs)[0]
        top_idxs = similarities.argsort(descending=True)[:max_per_section]

        for i, idx in enumerate(top_idxs, start=1):
            subsections.append({
                "document": section["source"],
                "page": section["page"],
                "refined_text": lines[idx],
                "importance_rank": i
            })

    return
