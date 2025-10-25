from .base_agent import BaseAgent
from core import llm_load, load_prompt, load_memory, ChatOutput
import os
from chains import chat_chain

class ChatAgent (BaseAgent):
    def __init__(self):
        self.chain = chat_chain.create_chat_chain()
        self.memory = load_memory("chat_history")

    def run(self, user_input: str) -> str:
        # 获取历史对话
        chat_history = self.memory.chat_memory  # 会返回之前的对话列表或字符串
        """
        调用 chain 处理输入并返回模型输出
        """
        # 直接调用 chain.run()
        result: ChatOutput = self.chain.invoke({
            "input": user_input,
            "chat_history": chat_history
        })

         # 更新 memory
        self.memory.save_context(
            {"input": user_input},
            {"output": result.output}
        )
        return result.output

def get_ai_reply(msg:str) -> str:
    agent = ChatAgent()
    response = agent.run(msg)
    return response