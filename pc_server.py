import os
import subprocess
import pyautogui
from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv
import uvicorn

load_dotenv()
app = FastAPI()
SECRET_TOKEN = os.getenv("AUTH_TOKEN")

class Command(BaseModel):
    action: str
    params: str = ""

@app.post("/execute")
async def execute(cmd: Command, x_token: str = Header(None)):
    if x_token != SECRET_TOKEN:
        raise HTTPException(status_code=401, detail="Unauthorized")
    
    print(f"Executing: {cmd.action} with {cmd.params}")
    
    if cmd.action == "open":
        subprocess.Popen(cmd.params, shell=True)
        return {"status": "success", "msg": f"Opened {cmd.params}"}
    
    elif cmd.action == "screenshot":
        pyautogui.screenshot("screen.png")
        return {"status": "success", "msg": "Screenshot taken"}
    
    return {"status": "error", "msg": "Unknown action"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)