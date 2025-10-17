from langchain.memory import ConversationBufferMemory

_memory_instance = None

def load_memory(key: str):
    global _memory_instance
    if _memory_instance is None:
        # 指定输入输出 key
        _memory_instance = ConversationBufferMemory(
            memory_key=key,
            input_key="question",
            output_key="answer",
            return_messages=True,
        )
    return _memory_instance