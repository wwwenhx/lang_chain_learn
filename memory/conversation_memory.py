from langchain.memory import ConversationBufferMemory

class ConversationMemory:
    def __init__(self, memory_key: str):
        self.memory = ConversationBufferMemory(memory_key=memory_key, return_messages=True)

    def get_memory(self):
        return self.memory