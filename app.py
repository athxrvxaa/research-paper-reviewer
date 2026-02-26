import streamlit as st
from utils.pdf_extractor import extract_text_from_pdf
from utils.text_cleaner import clean_text, remove_references_section
from utils.section_splitter import split_into_sections
from utils.gemini_model import GeminiReviewer

st.set_page_config(page_title="AI Research Paper Reviewer", layout="wide")

st.title("AI Research Paper Reviewer (LLaMA 3 Powered)")

uploaded_file = st.file_uploader("Upload Research Paper PDF", type="pdf")

if uploaded_file:

    with st.spinner("Processing..."):

        raw_text = extract_text_from_pdf(uploaded_file)
        cleaned_text = clean_text(raw_text)
        main_text = remove_references_section(cleaned_text)

        sections = split_into_sections(main_text)

        reviewer = GeminiReviewer()

        abstract = sections.get("abstract", "")[:1500]
        methodology = sections.get("methodology", "")[:1500]
        results = sections.get("results", "")[:1500]

        prompt = f"""
You are a strict academic peer reviewer.

Analyze the research paper information below and generate a structured review in this format:

### Summary
(Concise technical summary)

### Strengths
- Bullet points

### Weaknesses
- Bullet points

### Methodology Evaluation
(Technical critique)

### Suggestions for Improvement
- Bullet points

### Final Recommendation
(Choose one: Accept / Minor Revision / Major Revision / Reject and justify)

Abstract:
{abstract}

Methodology:
{methodology}

Results:
{results}
"""

        response = reviewer.generate(prompt)

        st.subheader("AI Review Output")
        st.write(response)