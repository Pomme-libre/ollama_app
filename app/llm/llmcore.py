import ollama


class Model():
    def __init__(self, text):
        self.text = text
        # self.model = "llama3.2:3b"
        self.model = "hf.co/bartowski/Llama-3.2-1B-Instruct-GGUF:Q4_K_M"

    def main(self):
        response = ollama.chat(
                model = self.model,
                messages = [{"role": "user", "content": self.text}]
                )
        return response["message"]["content"]
