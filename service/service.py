# server.py
from fastapi import FastAPI
from pydantic import BaseModel
from agents import get_ai_reply
import pyperclip

app = FastAPI()

class MessageRequest(BaseModel):
    text: str

class MessageResponse(BaseModel):
    reply: str

@app.post("/reply", response_model=MessageResponse)
async def get_reply(req: MessageRequest):
    reply = get_ai_reply(req.text)
    pyperclip.copy(reply)  # 将文本放入剪贴板
    print(req.text)
    print(reply)
    return {"reply": reply}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)