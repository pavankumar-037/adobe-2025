# schema.py

schema = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "title": {
            "type": "string",
            "description": "The document title, extracted from metadata or inferred from the first page."
        },
        "outline": {
            "type": "array",
            "description": "An ordered list of headings (H1–H3) found in the document.",
            "items": {
                "type": "object",
                "properties": {
                    "level": {
                        "type": "string",
                        "enum": ["H1", "H2", "H3"],
                        "description": "Heading level."
                    },
                    "text": {
                        "type": "string",
                        "description": "The heading text."
                    },
                    "page": {
                        "type": "integer",
                        "minimum": 1,
                        "description": "Page number where the heading appears."
                    }
                },
                "required": ["level", "text", "page"],
                "additionalProperties": False
            }
        }
    },
    "required": ["title", "outline"],
    "additionalProperties": False
}
