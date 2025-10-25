from langchain.memory import ConversationBufferWindowMemory

_memory_instance = None

def load_memory(key: str):
    global _memory_instance
    if _memory_instance is None:
        # 指定输入输出 key
        _memory_instance = ConversationBufferWindowMemory(
            memory_key=key,
            input_key="input",
            output_key="output",
            return_messages=True,
            k=10
        )
    return _memory_instance