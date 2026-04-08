# 🤖 Self-Operating Computer

**Control your PC from your phone using Gemini AI as the brain.** This project transforms your PC into a central server, your phone into a command center, and Google Gemini as the intelligent connector that translates natural language into system actions.

## 🏗️ Architecture

The system operates in a three-layer architecture:

1.  **Command Center (Mobile):** Uses Telegram as the interface to send voice or text commands.
2.  **The Brain (Gemini AI):** Processes the natural language, understands intent, and triggers specific functions.
3.  **Central Server (PC):** A FastAPI/Flask listener that stays active on your computer to execute authorized commands.

## 🌟 Features

- **Natural Language Control:** No need for specific syntax. Say "Open Chrome" or "Screenshot please," and it works.
- **Secure Execution:** Token-based authentication ensures only you can control your PC.
- **Remote Access:** Control your PC from anywhere in the world via secure tunneling (Ngrok).
- **Extensible:** Easily add custom scripts for media control, file management, or system monitoring.

## 📂 Project Structure

```
gemini-commander/

├── pc_server.py       # The Listener (FastAPI server running on PC)
├── ai_bridge.py       # The Connector (Telegram Bot + Gemini Logic)
├── .env               # API Keys and Secret Tokens (Private)
└── README.md          # Project documentation
```

## ⚙️ Setup & Installation

### 1\. Prerequisites

- Python 3.9+ installed.
- A Telegram Bot Token (from [@BotFather](https://www.google.com/search?q=https://t.id/botfather)).
- A Gemini API Key (from [Google AI Studio](https://aistudio.google.com/)).

### 2\. Installation

Clone the repository and install dependencies:

```
git clone https://github.com/yourusername/gemini-pc-commander.git  cd gemini-pc-commander  pip install -r requirements.txt
```

### 3\. Configuration

Create a .env file in the root directory:

```
GEMINI_API_KEY=your_gemini_key_here  TELEGRAM_BOT_TOKEN=your_telegram_bot_token_here  AUTH_TOKEN=choose_a_strong_secret_password  PC_SERVER_URL=your_ngrok_url_here
```

## ▶️ Running the Project

1.  Bashpython pc_server.py
2.  Bashngrok http 8000*Copy the Forwarding URL and update PC_SERVER_URL in your .env.*
3.  Bashpython ai_bridge.py

## 🧪 Usage Examples

Open your Telegram bot and try these:

- "Open Notepad"
- "Take a screenshot"
- "Lock my workstation"
- "Open Chrome and go to YouTube"

## 🔐 Security Information

- **Authentication:** All requests from the AI Bridge to the PC Server require an X-Token header.
- **Privacy:** It is recommended to whitelist your Telegram User ID in ai_bridge.py so others cannot message your bot.
- **Local Safety:** Use pyautogui and subprocess carefully to avoid accidental system changes.

## 🛠️ Troubleshooting

- **404 Model Not Found:** Ensure your google-generativeai library is updated (pip install -U google-generativeai).
- **Connection Refused:** Ensure Ngrok is pointing to the correct port (default: 8000) and your firewall allows local connections.

## 📜 License

This project is licensed under the MIT License - see the LICENSE file for details.
