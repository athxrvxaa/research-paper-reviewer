import streamlit as st
from utils.pdf_extractor import extract_text_from_pdf
from utils.text_cleaner import clean_text, remove_references_section
from utils.section_splitter import split_into_sections
from utils.summarizer import PaperSummarizer
from utils.reviewer import PaperReviewer

st.set_page_config(page_title="AI Research Paper Reviewer", layout="wide")

st.title("AI Research Paper Reviewer")

uploaded_file = st.file_uploader("Upload Research Paper PDF", type="pdf")

if uploaded_file:

    with st.spinner("Processing PDF..."):

        # --------- TEXT EXTRACTION ----------
        raw_text = extract_text_from_pdf(uploaded_file)
        cleaned_text = clean_text(raw_text)
        main_text = remove_references_section(cleaned_text)

        # --------- SECTION SPLITTING ----------
        sections = split_into_sections(main_text)

        # --------- LOAD MODELS (CACHED) ----------
        summarizer = PaperSummarizer()
        reviewer = PaperReviewer()

        # --------- SUMMARY ----------
        st.subheader("Generated Summary")

        if sections.get("abstract") and sections["abstract"].strip() != "":
            summary = summarizer.summarize_text(sections["abstract"])
        else:
            # fallback: summarize limited portion for speed
            short_text = main_text[:3000]
            summary = summarizer.summarize_text(short_text)

        st.write(summary)

        # --------- REVIEW GENERATION ----------
        st.subheader("Generated Review")

        methodology_text = sections.get("methodology", "")[:1500]
        results_text = sections.get("results", "")[:1500]

        prompt = f"""
You are an academic peer reviewer.

Based on the information below, provide:

1. Key Strengths
2. Key Weaknesses
3. Evaluation of Methodology
4. Suggestions for Improvement
5. Overall Recommendation (Accept / Minor Revision / Major Revision / Reject)

Paper Summary:
{summary}

Methodology Section:
{methodology_text}

Results Section:
{results_text}
"""

        review = reviewer.generate_review(prompt)

        st.write(review)