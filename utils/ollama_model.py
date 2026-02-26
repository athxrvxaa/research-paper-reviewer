import requests


class OllamaReviewer:
    def __init__(self, model="mistral"):
        self.model = model
        self.url = "http://localhost:11434/api/generate"

    def generate(self, prompt):

        response = requests.post(
            self.url,
            headers={"Content-Type": "application/json"},
            json={
                "model": self.model,
                "prompt": prompt,
                "stream": False,
                "options": {
                    "temperature": 0.7,
                    "num_predict": 400
                }
            }
        )

        if response.status_code != 200:
            return f"Error: {response.text}"

        return response.json().get("response", "No response")