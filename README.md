# emmi-letschat


A real-time chat app built with Python, Flask, and Socket.IO — running on a Raspberry Pi as a mini home server.

---

This is a learning project where I built:

* 🔐 Login system (basic authentication)
* 💬 Real-time chat using WebSockets
* 🗄️ Persistent message storage (SQLite)
* 🌐 Web interface accessible from multiple devices on the same network
* 🍓 Hosted on a Raspberry Pi Zero 2 W

---

## What I learned

This project helped me understand:

* How client-server communication actually works
* The difference between HTTP and WebSockets
* How identity works in networking (sessions vs usernames vs connections)
* How databases store and retrieve structured data
* How to host a service on a local network device

---

## Tech Stack

* Python 
* Flask 
* Flask-SocketIO 
* SQLite 
* HTML / JavaScript 
* Raspberry Pi 

---

## ⚙️ How to run it

### 1. Clone or copy the project

```bash
cd emmi-letschat
```

### 2. Create virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install flask flask-socketio
```

### 4. Run the server

```bash
python app.py
```

### 5. Open in browser

```
http://<your-pi-ip>:5000
```

---

## 🔐 Login system (demo credentials)

This project currently uses a simple demo login system:

* username: `angxl` | password: `1234`
* username: `admin` | password: `admin`

⚠️ These are NOT secure and are only for learning.

---

## Features

* Real-time messaging across devices
* Persistent chat history (stored in SQLite)
* Session-based login system
* Works on local WiFi network
* Runs on low-power hardware (Raspberry Pi)

---

## ⚠️ Limitations

This is a learning project, so it has some intentional limitations:

* Passwords are not hashed yet
* No encryption (HTTP only)
* No production-level authentication
* No message editing or deletion
* No user roles or permissions

---

## Future ideas

Things I might add next:

*  Password hashing (real security)
*  Multiple chat rooms
*  Mobile-friendly UI
*  Improve UI design
*  Online/offline user status
*  Message timestamps

---

## Why I built this

I wanted to understand how apps like Discord or WhatsApp Web actually work under the hood — not just use them, but build a tiny version of them from scratch.

---

## Fun fact

This entire chat system runs on a tiny Raspberry Pi acting like a mini server sitting on my network.

---

## Notes

If you're reading this and trying to build it yourself:

Don’t rush. Break things. Fix them. That’s how you actually learn networking.

---

##  License

Free to use, break, and rebuild for learn
