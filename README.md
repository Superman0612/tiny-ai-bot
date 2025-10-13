🧠 Tiny AI-Powered Q&A Bot

A simple **AI-powered Question & Answer bot** built in Python using **Google Gemini API**.  
This project was created as part of an assignment to learn about APIs, command-line apps, and building simple UIs.

---

🚀 Features
- Ask any question from the command line and get AI-generated answers.
- Simple **Streamlit UI** for web-based interaction.
- Uses **Gemini 2.5 Flash Lite** model.
- Documented all errors & fixes during development.

---

⚙️ Setup Instructions

### 1. Install Python
Check if Python is installed:
bash
python --version

2. Clone the Repo
git clone https://github.com/<Superman0612>/tiny-ai-bot.git
cd tiny-ai-bot

3. Create Virtual Enviornment(Optional but Recommended)
python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate  # Mac/Linux

4. install Dependecies
pip install -r requirements.txt

5. Set APi Key
create a .env file in the project root:
GEMINI_API_KEY=AIzaSyAl8V3b1lf_FPEAA1gBSvyWpM0Atn9RblM

▶️ How to Run
1. Command-Line Version
python app.py
Type your question and get AI-generated answers.

2. Streamlit UI Version
python -m streamlit run ui.py
Open the browser link shown in terminal(Usually http://localhost:8501 ) and ask questions there.

📚 Learnings
1. How to integrate Gemini API in Pyhthon.
2. Difference between CLI and UI-based apps.
3. How to set up a Python project with dependencies and enviornment variables.
5. How to document your prjoect properly.


👤 Author
Name: Shubham Devatwal
Assignment: Tiny-AI-Bot
Date: 04-oct-2025


