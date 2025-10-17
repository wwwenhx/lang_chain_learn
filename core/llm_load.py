from langchain import chat_models
import os
from configs import DEPLOYMENT_NAME
import threading

# 单例变量
_model_instance = None
_lock = threading.Lock()  # 保证多线程安全

def llm_load():
    global _model_instance
    if _model_instance is None:
        with _lock:
            if _model_instance is None:
                _model_instance = chat_models.init_chat_model(model=DEPLOYMENT_NAME, model_provider="azure_openai")
    return _model_instance