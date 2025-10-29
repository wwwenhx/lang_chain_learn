from .base_agent import BaseAgent
from core import llm_load, load_prompt, load_memory, ChatOutput
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
        result: ChatOutput = self.chain.invoke({
            "input": user_input,
        })
        return result.output

def get_ai_reply(msg:str) -> str:
    agent = ChatAgent()
    response = agent.run(msg)
    return response