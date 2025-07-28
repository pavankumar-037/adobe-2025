def build_output(persona, job, documents, timestamp, section_results, subsection_results):
    output = {
        "metadata": {
            "persona": persona,
            "job": job,
            "documents": documents,
            "timestamp": timestamp
        },
        "section_analysis": [],
        "subsection_analysis": []
    }

    for section in section_results:
        output["section_analysis"].append({
            "document": section["source"],
            "page": section["page"],
            "section_title": "",  # Not extracted yet — placeholder
            "importance_rank": section["importance_rank"]
        })

    for sub in subsection_results:
        output["subsection_analysis"].append({
            "document": sub["document"],
            "page": sub["page"],
            "refined_text": sub["refined_text"],
            "importance_rank": sub["importance_rank"]
        })

    return output
