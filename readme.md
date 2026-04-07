# 🧠 AI Remote PC Control (Telegram + Gemini)

Control your PC remotely using natural language commands via Telegram.
This system uses **Google Gemini AI** to convert human text into executable commands and runs them on your PC.

---

## 🚀 System Flow

```
Telegram → Bridge Server → Gemini AI → Command → PC Listener → Output → Telegram
```

---

## 📦 Features

- 📱 Control PC from Telegram
- 🤖 Natural language → system command
- ⚡ Real-time execution
- 🔐 Token-based security
- 🧩 Modular architecture

---

## 🏗️ Project Structure

```
project/
│
├── listener.py   # Runs on PC (executes commands)
├── ai.py         # Gemini AI logic
├── bridge.py     # Telegram + AI + PC connector
└── run.sh        # (optional) start script
```

---

## ⚙️ Setup Guide

### 1️⃣ Clone Repository

```
git clone https://github.com/yourusername/ai-remote-pc.git
cd ai-remote-pc
```

---

### 2️⃣ Install Dependencies

```
pip install flask requests python-telegram-bot google-generativeai
```

---

### 3️⃣ Configure Environment

Edit files:

#### 📄 `listener.py`

```
SECRET = "your_strong_secret_here"
```

#### 📄 `ai.py`

```
genai.configure(api_key="YOUR_GEMINI_API_KEY")
```

#### 📄 `bridge.py`

```
PC_URL = "http://YOUR_PC_IP:5000/run"
SECRET = "your_strong_secret_here"
BOT_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
```

---

## ▶️ Run the System

### Option A: Manual

```
python listener.py
```

Open another terminal:

```
python bridge.py
```

---

### Option B: Bash Script (Linux/Mac)

```
chmod +x run.sh
./run.sh
```

---

### Option C: Windows

Create `run.bat`:

```
@echo off
start cmd /k python listener.py
timeout /t 2
start cmd /k python bridge.py
```

---

## 📱 Telegram Bot Setup

1. Open Telegram
2. Search **BotFather**
3. Run `/start`
4. Create bot → `/newbot`
5. Copy your BOT TOKEN

---

## 🧪 Usage

Send commands in Telegram:

```
open notepad
```

```
shutdown pc
```

```
open chrome
```

---

## 🔐 Security Warning

⚠️ This system gives full control over your PC.

- Use a strong SECRET
- Do NOT expose port 5000 publicly
- Use firewall / VPN
- Add command filtering (recommended)
- Restrict Telegram user IDs

---

## ❗ Troubleshooting

| Problem            | Solution                      |
| ------------------ | ----------------------------- |
| Bot not responding | Check BOT_TOKEN & bridge.py   |
| No output          | Ensure listener.py is running |
| Unauthorized       | SECRET mismatch               |

---

## 💡 Future Improvements

- ✅ Command whitelist
- 🔐 User authentication
- 📊 Logging system
- 🌐 Web dashboard
- ☁️ Cloud deployment

---

## 📜 License

MIT License

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!

---
