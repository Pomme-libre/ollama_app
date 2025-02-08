import ollama

import time


class Model():
    def __init__(self, text):
        self.text = text
        self.model = "deepseek-r1:1.5b"

    def main(self):
        response = ollama.chat(
                model = self.model,
                messages = [
                    {
                        "role": "user",
                        "content": self.text,
                        }
                    ]
                )
        return response["message"]["content"]


def main():
    """/*************  ✨ Codeium Command ⭐  *************/
    Executes a chat request to the ollama service with a predefined user message
    and prints the content of the response message.

    The function sends a message to a chat model and expects a response that
    includes an explanation of why the sky is blue.

    /******  7448968d-51d5-4f61-882d-ed3ef567b18a  *******/
    """

    print("What is Model Number?")
    print("1: Llama3.2:1b")
    print("2: Llama3.2:3b")
    print("3: DeepSeek-R1:1.5b")
    get_model_number = input("> ")

    print("What is Question?")
    get_question = input("> ")

    # Default Model Name
    model_name = "deepseek-r1:1.5b"

    match int(get_model_number):
        case 1:
            model_name = "llama3.2:1b"
        case 2:
            model_name = "llama3.2:3b"
        case 3:
            model_name = "deepseek-r1:1.5b"
        case _:
            print("Please Enter Number in List!")

    time.sleep(2)

    response = ollama.chat(
        model = model_name,
        messages = [
            {
                "role": "user",
                "content": get_question,
                }
            ]
        )
    
    print(response["message"]["content"])


if __name__ == "__main__":
    main()
