# 🏥 Medical AI Assistant — MedBot

<div align="center">

![Python](https://img.shields.io/badge/Python-3.13-blue?style=for-the-badge&logo=python)
![Flask](https://img.shields.io/badge/Flask-3.1-black?style=for-the-badge&logo=flask)
![Groq](https://img.shields.io/badge/Groq-LLaMA_3.3_70B-orange?style=for-the-badge)
![HTML](https://img.shields.io/badge/HTML5-CSS3-red?style=for-the-badge&logo=html5)
![JavaScript](https://img.shields.io/badge/JavaScript-ES6-yellow?style=for-the-badge&logo=javascript)

**An AI-powered Medical Chatbot that answers health and medical questions only.**  
Built with Python, Flask, and Groq AI — featuring a professional ChatGPT-style interface.

</div>

---

## 👥 Group Members

| Name | Role |
|------|------|
| **Numair Iqbal** | Full Stack Development, AI Integration |
| **Nasir Amin** | Frontend Design, Testing & Documentation |

**University:** University of Layyah  
**Department:** Computer Science  
**Semester:** 6th Semester — Session 2025-2026  
**Subject:** Artificial Intelligence  

---

## 📌 Project Overview

**MedBot** is a specialized Medical AI Assistant that uses the **Groq API** powered by **LLaMA 3.3 70B** — one of the most powerful Large Language Models available. The chatbot is strictly limited to medical and health-related topics only. Any non-medical query is automatically blocked with a polite message.

> **Teacher Requirement:** Build an AI project that serves a single specific purpose.  
> **Our Solution:** A Medical-only AI Chatbot — MedBot.

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🏥 **Medical Only** | Strictly answers health and medical questions — all other topics blocked |
| 💬 **ChatGPT-Style UI** | Professional dark theme with sidebar, chat history, and action buttons |
| 💾 **Permanent History** | All conversations saved in JSON file — preserved after laptop restart |
| 🌐 **Multi-Language** | Responds in English, Roman Urdu, or Urdu — matches user's language |
| 📱 **Mobile Access** | Accessible from any mobile device on the same WiFi network |
| 🔄 **Retry Logic** | Automatically retries 3 times on connection error |
| ⏰ **Timestamps** | Every message shows time sent |
| 📋 **Copy & Like** | Copy, like, dislike, and regenerate buttons on every response |
| 🔍 **Search Chats** | Search through all previous conversations |
| 🚨 **Emergency Alert** | Every response reminds users to call 1122 for emergencies in Pakistan |

---

## 🛠️ Technologies Used

| Technology | Version | Purpose |
|-----------|---------|---------|
| Python | 3.13 | Backend programming language |
| Flask | 3.1.3 | Web server framework |
| Flask-CORS | 5.0.1 | Cross-Origin Resource Sharing |
| Groq API | Latest | AI intelligence engine |
| LLaMA 3.3 70B | Latest | Large Language Model |
| HTML5 | Latest | Frontend structure |
| CSS3 | Latest | Styling and dark theme |
| JavaScript | ES6 | Frontend interactivity |
| JSON | — | Permanent chat history storage |

---

## 📁 Project Structure

```
AI_Chatbot/
├── app.py                  # Flask backend server + Groq AI integration
├── index.html              # Frontend HTML structure
├── style.css               # Professional dark theme CSS
├── script.js               # Frontend JavaScript + API calls
├── chat_history.json       # Permanent chat history storage
└── README.md               # Project documentation
```

---

## ⚙️ System Architecture

```
User (Browser)
     ↓
index.html + style.css + script.js
     ↓  (HTTP POST)
Flask Backend — app.py (Port 5000)
     ↓  (API Call)
Groq API — LLaMA 3.3 70B
     ↓  (Response)
Flask Backend
     ↓
Browser — Chat Bubble Displayed
```

---

## 🚀 How to Run

### Step 1 — Install Required Libraries

```bash
pip install flask flask-cors groq
```

### Step 2 — Add Your Groq API Key

Open `app.py` and replace the API key:

```python
client = Groq(api_key="YOUR_GROQ_API_KEY_HERE")
```

Get your free API key from: [console.groq.com](https://console.groq.com)

### Step 3 — Run the Server

```bash
py -3.13 app.py
```

### Step 4 — Open in Browser

Open VS Code → Click **"Go Live"** on `index.html`

Or open your browser and go to:

```
http://127.0.0.1:5500
```

### Step 5 — Access on Mobile (Optional)

Make sure your PC and mobile are on the same WiFi.  
Find your PC's IP address:

```bash
ipconfig
```

Then open on mobile browser:

```
YOUR_IP_ADDRESS:5500
```

---

## 🧪 Testing Results

| Test Query | Expected Result | Status |
|-----------|----------------|--------|
| What are symptoms of fever? | Detailed medical answer | ✅ PASSED |
| What is diabetes? | Medical explanation | ✅ PASSED |
| How to treat a headache? | Treatment advice | ✅ PASSED |
| Blood pressure symptoms? | Medical answer | ✅ PASSED |
| What is Artificial Intelligence? | Blocked — not medical | ✅ BLOCKED |
| Pakistan ka capital kya hai? | Blocked — not medical | ✅ BLOCKED |
| Mobile browser access | Chatbot accessible | ✅ PASSED |

---

## ⚠️ Challenges & Solutions

| Challenge | Solution |
|-----------|----------|
| CORS error — API blocked from browser | Built Flask backend to handle all API requests |
| Gemini API rate limit exceeded | Switched to Groq API — no strict daily limits |
| Python 3.14 corruption — tempfile error | Reinstalled Python 3.13 with correct PATH |
| Mobile access not working | Configured Flask with `host='0.0.0.0'` |
| Empty chats appearing in sidebar | Added filter — only chats with messages shown |

---

## 📸 Screenshots

> Live Demo available — run the project locally to see the full interface.

**Key UI Features:**
- Professional dark sidebar with chat history
- Medical-only responses with emergency reminders
- Welcome screen with quick question buttons
- Typing animation — "MedBot is thinking..."

---

## 🔮 Future Enhancements

- [ ] Voice input support
- [ ] User login and registration system
- [ ] Cloud deployment (Render / Heroku)
- [ ] Database integration (SQLite / MongoDB)
- [ ] Appointment booking feature
- [ ] Multi-doctor specialization support

---

## 📄 License

This project was developed for academic purposes at the **University of Layyah** as part of the **Artificial Intelligence** course.

---

## 🙏 Acknowledgements

- [Groq](https://groq.com) — For providing fast and free AI API
- [Meta AI](https://ai.meta.com) — For LLaMA 3.3 70B model
- [Flask](https://flask.palletsprojects.com) — For the lightweight web framework
- University of Layyah — Computer Science Department

---

<div align="center">

**Made with ❤️ by Numair Iqbal & Nasir Amin**  
**University of Layyah — 6th Semester — 2025-2026**

</div>
