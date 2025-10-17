from core import llm_load, load_prompt, load_memory
import os
from langchain.chains.llm import LLMChain
from langchain.prompts import MessagesPlaceholder

def create_chat_chain():
    model = llm_load()
    prompt = load_prompt("chat")
    memory = load_memory("chat_history")

    chat_chain = LLMChain(
        llm=model,
        prompt=prompt,
        memory=memory,
        output_key="answer",
    )

    return chat_chain