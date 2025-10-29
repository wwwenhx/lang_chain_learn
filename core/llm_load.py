from langchain import chat_models
from langchain_openai import ChatOpenAI
import os
from configs import APK_API_KEY
import threading

# 单例变量
_model_instance = None
_lock = threading.Lock()  # 保证多线程安全

def llm_load():
    global _model_instance
    if _model_instance is None:
        with _lock:
            if _model_instance is None:
                _model_instance = ChatOpenAI(
                    model="bot-20251029152124-pqkmc",
                    base_url="https://ark.cn-beijing.volces.com/api/v3/bots",
                    api_key=APK_API_KEY,
                )
    return _model_instance