from flask import Flask, render_template, request, jsonify
from openai import OpenAI
from dotenv import load_dotenv
import os

# Load .env file and get API key
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Initialize OpenAI client
client = OpenAI(api_key=api_key)

# Create Flask app
app = Flask(__name__)

# Home route - renders HTML page
@app.route("/")
def home():
    return render_template("index.html")

# Chat endpoint - handles AJAX request
@app.route("/ask", methods=["POST"])
def ask():
    user_message = request.form["message"]

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that answers clearly and concisely."},
            {"role": "user", "content": user_message}
        ],
        temperature=0.7
    )

    bot_reply = response.choices[0].message.content.strip()
    return jsonify({"reply": bot_reply})

if __name__ == "__main__":
    app.run(debug=True)
