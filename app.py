import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load API key
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Pick a model
model = genai.GenerativeModel("gemini-2.5-flash-lite")

def ask_bot(question):
    response = model.generate_content(question)
    return response.text

if __name__ == "__main__":
    print("Welcome to Tiny AI Q&A Bot (Gemini Edition)! Type 'exit' to quit.")
    while True:
        q = input("You: ")
        if q.lower() == "exit":
            break
        try:
            print("Bot:", ask_bot(q))
        except Exception as e:
            print("Error:", e)

