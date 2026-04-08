from flask import Flask, request
import pyautogui
import os
import webbrowser

app = Flask(__name__)

def run_command(cmd):
    cmd = cmd.lower()

    if "open chrome" in cmd:
        os.system("start chrome")

    elif "youtube" in cmd:
        webbrowser.open("https://youtube.com")

    elif "shutdown" in cmd:
        os.system("shutdown /s /t 5")

    elif "type" in cmd:
        text = cmd.replace("type", "")
        pyautogui.write(text)

@app.route("/run", methods=["POST"])
def run():
    data = request.json
    cmd = data.get("command", "")
    print("Command:", cmd)

    run_command(cmd)
    return {"status": "done"}

app.run(host="0.0.0.0", port=5000)