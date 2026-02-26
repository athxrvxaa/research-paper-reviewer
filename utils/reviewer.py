import torch
import streamlit as st
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM


@st.cache_resource
def load_reviewer_model():
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model_name = "google/flan-t5-large"

    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
    model.to(device)

    return tokenizer, model, device


class PaperReviewer:
    def __init__(self):
        self.tokenizer, self.model, self.device = load_reviewer_model()

    def generate_review(self, prompt):

        inputs = self.tokenizer(
            prompt,
            return_tensors="pt",
            truncation=True,
            max_length=2048
        ).to(self.device)

        outputs = self.model.generate(
            inputs["input_ids"],
            max_length=500,
            num_beams=2,  # reduced beams
            temperature=0.7,
            early_stopping=True
        )

        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)