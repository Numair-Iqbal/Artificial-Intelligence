from flask import Flask, request, jsonify
from flask_cors import CORS
from groq import Groq
import json
import os

app = Flask(__name__)
CORS(app)

# API key .env file se lega (safe for GitHub)
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

HISTORY_FILE = "chat_history.json"

def load_history():
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r") as f:
            return json.load(f)
    return {}

def save_history(data):
    with open(HISTORY_FILE, "w") as f:
        json.dump(data, f, indent=2)

@app.route("/chat", methods=["POST", "OPTIONS"])
def chat():
    if request.method == "OPTIONS":
        return "", 200
    
    data = request.json
    user_message = data.get("message", "")
    chat_id = data.get("chat_id", "default")

    if not user_message:
        return jsonify({"reply": "Please send a message."})

    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "system",
                    "content": """You are a Medical AI Assistant. Your name is MedBot.

🚨 RULE 1: MEDICAL ONLY
ONLY answer questions related to medicine and health.

If anyone asks anything outside of medical topics, respond with:
'I am a Medical AI Assistant. I can only help with health and medical questions.'

🚨 RULE 2: DISCLAIMER (MANDATORY)
At the END of EVERY answer, add this line:
'⚠️ DISCLAIMER: Main doctor nahi hoon. Ye general medical information hai. Emergency: 1122'

🚨 RULE 3: EMERGENCY FIRST
If user mentions: heart attack, accident, bleeding, seizure, emergency, chest pain, stroke
FIRST line of response MUST be:
'🚨 EMERGENCY! Turant 1122 ya 15 call karein.'

🚨 RULE 4: FOLLOW-UP QUESTION
After EVERY medical response (before disclaimer), ask ONE relevant follow-up question.

🚨 RULE 5: LANGUAGE
Always respond in the same language the user writes in."""
                },
                {"role": "user", "content": user_message}
            ]
        )

        reply = response.choices[0].message.content

        history = load_history()

        if chat_id not in history:
            history[chat_id] = {"title": user_message[:30], "messages": []}
        elif history[chat_id].get("title") == "New Chat":
            history[chat_id]["title"] = user_message[:30]

        history[chat_id]["messages"].append({"text": user_message, "isUser": True})
        history[chat_id]["messages"].append({"text": reply, "isUser": False})

        save_history(history)

        return jsonify({"reply": reply})

    except Exception as e:
        return jsonify({"reply": f"Technical error: {str(e)}"})

@app.route("/history", methods=["GET", "OPTIONS"])
def get_history():
    if request.method == "OPTIONS":
        return "", 200
    return jsonify(load_history())

@app.route("/new_chat", methods=["POST", "OPTIONS"])
def new_chat():
    if request.method == "OPTIONS":
        return "", 200
    data = request.json
    chat_id = data.get("chat_id")
    history = load_history()
    if chat_id not in history:
        history[chat_id] = {"title": "New Chat", "messages": []}
        save_history(history)
    return jsonify({"success": True})

@app.route("/delete_chat", methods=["POST", "OPTIONS"])
def delete_chat():
    if request.method == "OPTIONS":
        return "", 200
    data = request.json
    chat_id = data.get("chat_id")
    history = load_history()
    if chat_id in history:
        del history[chat_id]
        save_history(history)
    return jsonify({"success": True})

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False, use_reloader=False)
