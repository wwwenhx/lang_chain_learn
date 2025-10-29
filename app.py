from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from agents import ChatAgent

# 初始化 FastAPI 应用
app = FastAPI(title="ChatAgent API", version="1.0")

# 初始化你的智能体（只加载一次）
agent = ChatAgent()

# 定义请求体模型
class ChatRequest(BaseModel):
    message: str

# 定义响应模型
class ChatResponse(BaseModel):
    reply: str

@app.post("/chat", response_model=ChatResponse)
def chat_endpoint(request: ChatRequest):
    """
    接收用户输入并返回智能体回复
    """
    try:
        response = agent.run(request.message)
        return ChatResponse(reply=response)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
def root():
    return {"message": "ChatAgent API is running 🚀"}