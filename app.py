import sqlite3
from flask import Flask, render_template, request, redirect, session
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-change-this'
socketio = SocketIO(app, cors_allowed_origins="*")

users = {}

# ---------------- FAKE USER DATABASE (replace later with real DB) ----------------
fake_users = {
    "angxl": "1234",
    "admin": "admin"
    "jamal": "papajamal"
}

# ---------------- DATABASE SETUP ----------------
def init_db():
    conn = sqlite3.connect("chat.db")
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            message TEXT
        )
    """)
    conn.commit()
    conn.close()

init_db()

def save_message(username, message):
    conn = sqlite3.connect("chat.db")
    c = conn.cursor()
    c.execute("INSERT INTO messages (username, message) VALUES (?, ?)",
              (username, message))
    conn.commit()
    conn.close()

def load_messages():
    conn = sqlite3.connect("chat.db")
    c = conn.cursor()
    c.execute("SELECT username, message FROM messages")
    data = c.fetchall()
    conn.close()
    return [f"{u}: {m}" for u, m in data]

# ---------------- LOGIN ROUTE ----------------
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username in fake_users and fake_users[username] == password:
            session["user"] = username
            return redirect("/chat")

        return "Invalid login"

    return render_template("login.html")

# ---------------- CHAT PAGE (PROTECTED) ----------------
@app.route("/chat")
def index():
    if "user" not in session:
        return redirect("/")

    return render_template(
        "index.html",
        history=load_messages(),
        user=session["user"]
    )

# ---------------- SOCKET ----------------
@socketio.on("message")
def handle_message(msg):
    username = session.get("user", "Anonymous")

    full_msg = f"{username}: {msg}"

    save_message(username, msg)
    send(full_msg, broadcast=True)

# ---------------- DISCONNECT ----------------
@socketio.on("disconnect")
def disconnect():
    users.pop(request.sid, None)

# ---------------- RUN ----------------
if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=5000)