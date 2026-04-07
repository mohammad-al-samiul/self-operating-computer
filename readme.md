🧠 AI Remote PC Control (Telegram + Gemini) – Setup & Usage Guide
=================================================================

This guide will help you **install, configure, and use** the system step-by-step.

⚙️ 1. Prerequisites
-------------------

Make sure you have:

*   Python 3.9 or higher installed
    
*   A Telegram account
    
*   A Google Gemini API key
    
*   Your PC connected to the internet (same network or public access)
    

🔑 2. Get Required Keys
-----------------------

### 📱 Telegram Bot Token

1.  Open Telegram
    
2.  Search **BotFather**
    
3.  Type /start
    
4.  Type /newbot
    
5.  Set bot name and username
    
6.  Copy the **BOT TOKEN**
    

### 🤖 Gemini API Key

1.  Go to Google AI Studio
    
2.  Generate API key
    
3.  Copy it
    

📁 3. Project Setup
-------------------

Create a project folder and add these files:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   project/  │  ├── listener.py  ├── ai.py  ├── bridge.py   `

📦 4. Install Dependencies
--------------------------

Run this command in terminal:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   pip install flask requests python-telegram-bot google-generativeai   `

💻 5. Setup PC Listener (Main Engine)
-------------------------------------

Edit listener.py:

*   Change SECRET (important)
    

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   SECRET = "your_strong_secret_here"   `

Run:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   python listener.py   `

✅ Your PC is now listening on:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   http://localhost:5000/run   `

🌐 6. Find Your PC IP
---------------------

### Windows:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   ipconfig   `

Look for:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   IPv4 Address → example: 192.168.1.5   `

🤖 7. Setup AI (Gemini)
-----------------------

Edit ai.py:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   genai.configure(api_key="YOUR_GEMINI_API_KEY")   `

🔗 8. Setup Bridge Server
-------------------------

Edit bridge.py:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   PC_URL = "http://YOUR_PC_IP:5000/run"  SECRET = "your_strong_secret_here"  BOT_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"   `

▶️ 9. Run the System
--------------------

### Step 1: Start Listener (PC)

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   python listener.py   `

### Step 2: Start Bridge Server

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   python bridge.py   `

🧪 10. Test the System
----------------------

Open your Telegram bot and send:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   open notepad   `

✅ Expected flow:

1.  You send message
    
2.  Gemini converts → notepad
    
3.  Command sent to PC
    
4.  PC executes
    
5.  Output returned to Telegram
    

🔐 Security Tips (VERY IMPORTANT)
---------------------------------

⚠️ This system can fully control your PC

*   Use a strong SECRET (not mysecret123)
    
*   Do NOT expose port 5000 publicly without protection
    
*   Use firewall or VPN
    
*   Add command filtering (recommended)
    
*   Restrict Telegram user IDs
    

❗ Common Errors & Fix
---------------------

### ❌ Bot not responding

*   Check BOT\_TOKEN
    
*   Ensure bridge.py is running
    

### ❌ No output from PC

*   Check listener is running
    
*   Verify PC IP is correct
    

### ❌ Unauthorized error

*   SECRET mismatch between files
    

🚀 Example Commands
-------------------

Try sending:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   open chrome  shutdown pc  list files in desktop   `

🧠 How It Works
---------------

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   Telegram → Bridge → Gemini → Command → PC → Output → Telegram   `

💡 Future Improvements
----------------------

*   Add GUI dashboard
    
*   Add authentication system
    
*   Add command history
    
*   Add file transfer support
    

🎯 Done!
--------

You now have your own **AI-powered remote PC controller** 🤖💻

Use responsibly and securely.