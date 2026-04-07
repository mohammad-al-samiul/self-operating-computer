from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

SECRET = "mysecret123"

@app.route("/run", methods=["POST"])
def run_command():
    data = request.json

    if data.get("token") != SECRET:
        return jsonify({"error": "Unauthorized"}), 403

    cmd = data.get("cmd")

    try:
        result = subprocess.check_output(cmd, shell=True, text=True)
        return jsonify({"output": result})
    except Exception as e:
        return jsonify({"error": str(e)})

app.run(host="0.0.0.0", port=5000)