def extract_title(markdown: str) -> str:
    lines = markdown.split("\n\n")
    for li in lines:
        clean = li.strip()
        if len(clean) > 2 and clean[:2] == "# ":
            return clean[2:].strip()

    raise ValueError("markdown must contain a title")
