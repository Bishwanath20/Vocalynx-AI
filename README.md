# 🔊 Vocalynx AI

**Vocalynx AI** is a smart, voice-driven assistant designed for **urgent call dispatch**, emergency help, and real-time voice interaction. It integrates voice AI with a modern web interface and can be extended for healthcare, security alerts, or any responsive service.

---

## 🧠 Key Features

- ✅ Voice-based AI assistant powered by GPT-4.
- 📞 Real-time phone call capability using Omnidimension API.
- 🌐 Attractive web UI using HTML, Tailwind CSS, and JavaScript.
- 💬 Context-aware conversations via custom prompts.
- 📝 Automatic call logging for history/reference.
- 🔧 Easily customizable for different domains.

---

## 🚀 How It Works

1. User enters their **phone number** and **query** on the web interface.
2. Vocalynx AI uses the **Omnidimension API** to initiate a voice call.
3. The AI assistant **speaks the reply** in real time.
4. A log of the conversation is saved automatically.

---

## 🛠️ Tech Stack

- **Frontend**: HTML + Tailwind CSS + JavaScript
- **Backend**: Python + Flask
- **Voice API**: Omnidimension AI (Nova/Breeze)
- **Logs**: Text file (can be switched to a database)

---

## 📁 Project Structure

vocalynx-ai/
├── static/
│ ├── style.css # Tailwind or custom CSS
│ └── script.js # Call trigger JavaScript
├── templates/
│ └── index.html # Web interface
├── main.py # Python backend logic
├── call_logs.txt # Saved call logs
└── README.md

----

---

## 💻 Installation & Run

1.**Clone the repository
  
   git clone https://github.com/yourusername/vocalynx-ai.git
   cd vocalynx-ai
   
2.Install Python packages
     pip install flask requests
     
3.Add your Omnidimension API key
     api_key = "YOUR_OMNIDIMENSION_API_KEY"

4.Run the app
     python main.py
Open in browser
Go to http://localhost:5000 and test it.

------

📌 Use Cases
🚑 Emergency healthcare assistant
🧓 Elderly voice-based helper
🛡️ Real-time alert system
☎️ Smart customer support bot

----

🪪 License
This project is licensed under the MIT License – free to use, modify, and share.

👤 Author
Bishwanath Patra
GitHub: Bishwanath20
