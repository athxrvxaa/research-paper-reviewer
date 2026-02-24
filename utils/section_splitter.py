import re


def split_into_sections(text):
    """
    Detect sections using numbered headings like:
    1 Introduction
    2 Model Architecture
    3 Training
    4 Results
    5 Conclusion
    """

    # Regex for numbered headings
    heading_pattern = re.compile(
        r"(\n|\s)(\d+)\s+(Introduction|Related Work|Background|"
        r"Model|Model Architecture|Approach|Methods|Methodology|"
        r"Experiments|Results|Evaluation|Discussion|Conclusion)",
        re.IGNORECASE
    )

    matches = list(heading_pattern.finditer(text))

    sections = {
        "abstract": "",
        "introduction": "",
        "methodology": "",
        "results": "",
        "conclusion": ""
    }

    # Extract abstract separately (before first numbered section)
    if matches:
        first_section_start = matches[0].start()
        sections["abstract"] = text[:first_section_start].strip()

    for i, match in enumerate(matches):
        section_title = match.group(3).lower()
        start = match.end()

        if i + 1 < len(matches):
            end = matches[i + 1].start()
        else:
            end = len(text)

        content = text[start:end].strip()

        if section_title in ["introduction", "related work", "background"]:
            sections["introduction"] = content

        elif section_title in ["model", "model architecture", "approach", "methods", "methodology"]:
            sections["methodology"] = content

        elif section_title in ["experiments", "results", "evaluation", "discussion"]:
            sections["results"] = content

        elif section_title in ["conclusion"]:
            sections["conclusion"] = content

    return sections