import sqlite3
from flask import Flask, render_template, request
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
socketio = SocketIO(app)

users = {}

# ---------- DATABASE SETUP ----------
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

# ---------- ROUTES ----------
@app.route("/")
def index():
    return render_template("index.html", history=load_messages())

# ---------- SOCKET ----------
@socketio.on("set_username")
def set_username(username):
    users[request.sid] = username

@socketio.on("message")
def handle_message(msg):
    username = users.get(request.sid, "Anonymous")

    full_msg = f"{username}: {msg}"

    # save to DB (persistence)
    save_message(username, msg)

    # broadcast
    send(full_msg, broadcast=True)

@socketio.on("disconnect")
def disconnect():
    users.pop(request.sid, None)

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=5000)