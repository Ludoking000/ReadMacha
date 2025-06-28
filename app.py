from flask import Flask, render_template, request, jsonify
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

COHERE_API_KEY = os.getenv("lgMrg5O2nQdQBuJtWPMtdoD4tqJpQZNuLMJCnRwF")
COHERE_API_URL = "https://api.cohere.ai/v1/generate"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_msg = request.json.get("message")

    prompt = f"""You are ReadMAcHA, a cool Indian bro-style chatbot. Help students with career, exams, and studies. Be informal like 'macha', 'yo bro' but accurate.
Student: {user_msg}
ReadMAcHA:"""

    payload = {
        "model": "command-r-plus",
        "prompt": prompt,
        "max_tokens": 300,
        "temperature": 0.8
    }

    headers = {
        "Authorization": f"Bearer {COHERE_API_KEY}",
        "Content-Type": "application/json"
    }

    response = requests.post(COHERE_API_URL, headers=headers, json=payload)
    result = response.json()

    reply = result['generations'][0]['text'].strip() if 'generations' in result else "Sorry macha, something went wrong!"
    return jsonify({"reply": reply})

if __name__ == '__main__':
    app.run(debug=True)