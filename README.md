# AI-Based Research Paper Review Generator  
### MSc Data Science – Natural Language Processing Case Study (2025–26)

---

## Course Information
- Subject: CSD 670 – Data Science Practical VII  
- Domain: Natural Language Processing  
- Semester: IV  
- Institute: Fergusson College (Autonomous), Pune  
- Academic Year: 2025–26  

---

## Project Overview

The AI-Based Research Paper Review Generator is an NLP-driven system designed to automatically generate structured peer-review style feedback for academic research papers.

The system accepts a research paper in PDF format and produces:

- Concise summary of the paper  
- Key strengths  
- Identified weaknesses  
- Methodology evaluation  
- Overall quality score  
- Final recommendation (Accept / Minor Revision / Major Revision / Reject)

This project combines classical NLP techniques with modern Transformer-based models to simulate an academic peer-review process.

---

## Problem Statement

Peer-reviewing research papers is a time-consuming and subjective process. This project aims to develop an automated NLP-based system that:

- Extracts meaningful content from research papers
- Analyzes structure and methodology
- Generates structured review feedback
- Provides heuristic-based quality scoring

The goal is not to replace human reviewers, but to assist in preliminary evaluation and feedback generation.

---

## Core NLP Concepts Used

### 1. Text Preprocessing
- Tokenization
- Stopword removal
- Lemmatization
- Noise removal
- Section segmentation

### 2. Word & Sentence Embeddings
- Contextual embeddings
- Sentence similarity using cosine similarity

### 3. Transformer Architecture
- Self-attention mechanism
- Encoder-decoder models
- Pretrained language models

### 4. Abstractive Text Summarization
- Transformer-based summarization (BART / PEGASUS)

### 5. Prompt-Based Text Generation
- Instruction-tuned models (FLAN-T5)
- Structured review generation

### 6. Heuristic Scoring Mechanism
- Section presence analysis
- Keyword-based evaluation
- Readability and length-based scoring

---

## System Architecture
![Data Processing Pipeline](./img/workflow.png)

---

## Technologies and Libraries Used

### Core NLP
- transformers
- torch
- sentence-transformers
- nltk
- spacy
- scikit-learn

### PDF Processing
- PyMuPDF (fitz)

### Data Handling
- pandas
- numpy

### Evaluation
- rouge-score
- cosine similarity metrics

### Frontend Interface
- streamlit

---

## Output Structure

The system generates a structured review containing:
Summary
Strengths
Weaknesses
Methodology Evaluation
Overall Score (0–10)
Final Recommendation

---

## Evaluation Metrics

To validate performance:

- ROUGE Score for summarization quality
- Cosine similarity for semantic comparison
- Heuristic quality scoring
- Qualitative manual comparison with human-written reviews

---

## User Interface

The system is deployed using Streamlit, allowing users to:

- Upload a PDF research paper
- Automatically generate review
- View structured feedback in an interactive layout

---

## Project Structure
research-paper-reviewer/
│
├── app.py
├── utils/
│ ├── pdf_extractor.py
│ ├── text_cleaner.py
│ ├── section_splitter.py
│ ├── summarizer.py
│ ├── reviewer.py
│ ├── scorer.py
│
├── requirements.txt
└── README.md

---

## Future Enhancements

- Fine-tuning model on real peer-review datasets
- Multi-paper novelty comparison
- Plagiarism detection integration
- Graph-based citation analysis
- Reviewer bias detection
- Cloud deployment

---

## Expected Outcomes

- Demonstrates practical application of NLP in academia
- Integrates classical NLP and Transformer models
- Builds an end-to-end intelligent system
- Provides real-world research automation use-case

---

## References

- Vaswani et al., Attention Is All You Need
- Devlin et al., BERT: Pre-training of Deep Bidirectional Transformers
- Lewis et al., BART: Denoising Sequence-to-Sequence Pre-training
- Raffel et al., Exploring the Limits of Transfer Learning with T5

---

## Conclusion

This project showcases how modern NLP techniques and Transformer-based architectures can be applied to automate structured academic review generation. It bridges theoretical NLP foundations with real-world system implementation, making it a comprehensive case study in applied Natural Language Processing.