import torch
import streamlit as st
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM


@st.cache_resource
def load_summarizer_model():
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model_name = "facebook/bart-large-cnn"

    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
    model.to(device)

    return tokenizer, model, device


class PaperSummarizer:
    def __init__(self):
        self.tokenizer, self.model, self.device = load_summarizer_model()

    def summarize_text(self, text, max_length=180, min_length=60):

        inputs = self.tokenizer(
            text,
            return_tensors="pt",
            truncation=True,
            max_length=1024
        ).to(self.device)

        summary_ids = self.model.generate(
            inputs["input_ids"],
            max_length=max_length,
            min_length=min_length,
            num_beams=2,  # reduced beams for speed
            early_stopping=True
        )

        return self.tokenizer.decode(summary_ids[0], skip_special_tokens=True)