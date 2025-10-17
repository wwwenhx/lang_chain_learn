from .base_agent import BaseAgent
from core import llm_load, load_prompt, load_memory
import os
from chains import chat_chain

class ChatAgent (BaseAgent):
    def __init__(self):
        self.chain = chat_chain.create_chat_chain()

    def run(self, user_input: str) -> str:
        """
        调用 chain 处理输入并返回模型输出
        """
        # 直接调用 chain.run()
        result = self.chain.invoke({"question": user_input})
        return result["answer"]