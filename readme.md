# 💻📱 AI Remote PC Control (Gemini + Python)

Control your PC remotely using natural language from your mobile device powered by **Google Gemini AI**.

## 🚀 Overview

This project allows you to:

- 📱 Send commands from your phone
- 🤖 Convert natural language → Windows CMD using Gemini
- 🌐 Send commands via a server
- 💻 Execute commands on your PC automatically

## 🧠 How It Works

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   Mobile (User Input / Gemini)          ↓  Gemini AI (Text → Command)          ↓  Flask Server (Bridge)          ↓  PC Listener Script          ↓  Command Executed on PC   `

## 📂 Project Structure

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   project/   ├── server.py         # Web server + mobile UI   ├── listener.py       # PC command executor   ├── gemini_client.py  # AI command generator   └── README.md   `

## ⚙️ Requirements

- Python 3.8+
- Internet connection
- Windows OS (for CMD commands)

### 📦 Install Dependencies

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   pip install flask requests google-generativeai   `

## 🔑 Setup

### 1️⃣ Get Gemini API Key

- Go to Google AI Studio
- Generate API key
- Replace in code:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   genai.configure(api_key="YOUR_API_KEY")   `

### 2️⃣ Find Your PC IP

Run:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   ipconfig   `

Look for:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   IPv4 Address: 192.168.X.X   `

### 3️⃣ Update Config

Replace in files:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   SERVER_URL = "http://YOUR_IP:5000"   `

## ▶️ Run the System

### Step 1: Start Server

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   python server.py   `

### Step 2: Start Listener (PC)

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   python listener.py   `

### Step 3: Open Mobile UI

On your phone browser:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   http://YOUR_IP:5000   `

### Step 4: Send Commands

Type:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   open chrome and go to youtube   `

## 🤖 Gemini AI Usage

Gemini converts natural language into Windows commands.

### Example:

InputOutputopen chromestart chromeopen youtubestart chrome [https://youtube.com](https://youtube.com/)create folder testmkdir testlist filesdir

## 🔐 Security

⚠️ Important: This project allows remote execution.

### Implemented:

- Secret key validation
- Basic command filtering

### Recommended:

- Use strong secret key
- Restrict IP access
- Add HTTPS
- Avoid exposing to public internet

## 🧪 Safety Filter

Blocked commands:

- format
- del /f
- rd /s
- system destructive actions

## 📱 Mobile Control Options

### ✅ Web UI (Recommended)

- Open browser
- Enter commands directly

### ⚡ Gemini Assisted

- Use Gemini to generate commands
- Paste into UI

## 🚀 Features

- ✅ Natural language control
- ✅ AI-powered command generation
- ✅ Remote execution
- ✅ Context-aware memory
- ✅ Safety filtering

## 🔥 Future Improvements

- 🎤 Voice control (Jarvis mode)
- 📱 Telegram bot integration
- 🖥️ Screen automation (mouse/keyboard)
- 👀 AI screen reading
- 🌍 Internet-based control

## ⚠️ Disclaimer

Use at your own risk.Improper use may harm your system.

## 💡 Inspiration

Inspired by autonomous systems like:

- AI agents controlling computers
- Multimodal automation frameworks

## 🧑‍💻 Author

Built with ❤️ using Python + Gemini AI

## ⭐ Contribute

Pull requests welcome!

## 📜 License

MIT License
# self-operating-computer
