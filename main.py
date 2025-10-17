from agents import ChatAgent

def main():
    print("🤖 ChatAgent 启动成功，输入 'exit' 退出。\n")

    agent = ChatAgent()

    while True:
        user_input = input("👤 你：")
        if user_input.lower() in ["exit", "quit"]:
            print("👋 再见！")
            break

        try:
            response = agent.run(user_input)
            print(f"🤖 Agent：{response}\n")
        except Exception as e:
            print(f"⚠️ 出错了：{e}\n")

if __name__ == "__main__":
    main()