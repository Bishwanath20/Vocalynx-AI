from flask import Flask, render_template_string, redirect, url_for, flash
from omnidimension import Client
import datetime
import csv
import os

app = Flask(__name__)
app.secret_key = "super_secret_key"

# === Omnidimension API Setup ===
API_KEY = "YOUR_API_KEY"  # Replace this
YOUR_PHONE = "+919963607482"
AGENT_NAME = "Bish AI"

client = Client(api_key=API_KEY)

# === Call Logic ===
def dispatch_bish_call():
    try:
        context = [
            {"title": "Personality", "body": "You are Bish AI, a warm, honest assistant."},
            {"title": "Knowledge Scope", "body": "You help with code, AI, DSA, and general questions."},
            {"title": "Behavior", "body": "Be direct, avoid flattery, promote independence."}
        ]
        agent = client.agent.create(
            name=AGENT_NAME,
            voice="breeze",
            model="gpt-4",
            prompt="You are Bish AI...",
            temperature=0.7,
            transcription_model="whisper-large-v3",
            context_breakdown=context
        )
        agent_id = agent.get("json", {}).get("id")
        if not agent_id:
            raise Exception("Agent creation failed.")
        client.call.dispatch_call(agent_id=agent_id, to_number=YOUR_PHONE)
        log_call(AGENT_NAME, YOUR_PHONE)
        return "✅ Call initiated successfully!"
    except Exception as e:
        return f"❌ Call failed: {e}"

# === Logging ===
def log_call(agent, phone):
    with open("call_logs.csv", mode="a", newline='') as file:
        writer = csv.writer(file)
        writer.writerow([datetime.datetime.now(), agent, phone])

# === Routes ===
@app.route("/")
def index():
    return render_template_string("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Bish AI - Web Call</title>
        <script src="https://cdn.tailwindcss.com"></script>
        <script>
            setTimeout(() => {
                const alertBox = document.getElementById("flash-msg");
                if (alertBox) alertBox.style.display = "none";
            }, 3000);
        </script>
    </head>
    <body class="bg-gradient-to-br from-indigo-100 to-purple-200 min-h-screen flex items-center justify-center p-6">
        <div class="bg-white rounded-xl shadow-xl p-8 w-full max-w-lg text-center">
            <h1 class="text-3xl font-bold text-indigo-700 mb-6">📞 Call Bish AI</h1>

            {% with messages = get_flashed_messages() %}
              {% if messages %}
                <div id="flash-msg" class="bg-green-100 text-green-800 p-4 mb-6 rounded-md">
                    {{ messages[0] }}
                </div>
              {% endif %}
            {% endwith %}

            <a href="/call">
                <button class="bg-indigo-600 hover:bg-indigo-700 text-white font-semibold py-2 px-6 rounded-full shadow-md transition">
                    Trigger Call
                </button>
            </a>
            <a href="/logs" class="ml-4">
                <button class="bg-gray-200 hover:bg-gray-300 text-gray-700 font-semibold py-2 px-6 rounded-full shadow-md transition">
                    View Call Logs
                </button>
            </a>
        </div>
    </body>
    </html>
    """)

@app.route("/call")
def call():
    result = dispatch_bish_call()
    flash(result)
    return redirect(url_for("index"))

@app.route("/logs")
def logs():
    logs = []
    if os.path.exists("call_logs.csv"):
        with open("call_logs.csv", newline='') as f:
            logs = list(csv.reader(f))
    return render_template_string("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Call Logs</title>
        <script src="https://cdn.tailwindcss.com"></script>
    </head>
    <body class="bg-gray-100 min-h-screen flex items-center justify-center p-6">
        <div class="bg-white rounded-xl shadow-xl p-8 w-full max-w-4xl">
            <h2 class="text-2xl font-bold text-indigo-700 mb-6">📜 Call Logs</h2>
            <table class="min-w-full bg-white border border-gray-200 rounded-md">
                <thead>
                    <tr class="bg-indigo-100 text-indigo-800 font-semibold">
                        <th class="py-2 px-4 border">DateTime</th>
                        <th class="py-2 px-4 border">Agent</th>
                        <th class="py-2 px-4 border">Phone</th>
                    </tr>
                </thead>
                <tbody>
                    {% for log in logs %}
                    <tr class="hover:bg-gray-100 text-center">
                        <td class="py-2 px-4 border">{{ log[0] }}</td>
                        <td class="py-2 px-4 border">{{ log[1] }}</td>
                        <td class="py-2 px-4 border">{{ log[2] }}</td>
                    </tr>
                    {% endfor %}
                </tbody>
            </table>
            <div class="mt-6 text-center">
                <a href="/">
                    <button class="bg-indigo-600 hover:bg-indigo-700 text-white font-semibold py-2 px-6 rounded-full transition">
                        ⬅ Back
                    </button>
                </a>
            </div>
        </div>
    </body>
    </html>
    """, logs=logs)

if __name__ == "__main__":
    app.run(debug=True)
