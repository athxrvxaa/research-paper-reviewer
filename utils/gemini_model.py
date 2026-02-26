from google import genai
import streamlit as st


@st.cache_resource
def load_gemini():
    return genai.Client(api_key=st.secrets["GEMINI_API_KEY"])


class GeminiReviewer:
    def __init__(self):
        self.client = load_gemini()

    def generate(self, prompt):
        response = self.client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
        )
        return response.text