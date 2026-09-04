from agent_sage.agent import ChatAgent

ROUNDS = 5

agent_a = ChatAgent(
    name="Alice",
    system_prompt="You are a curious philosopher. Ask thoughtful questions and challenge ideas. Keep replies concise.",
)

agent_b = ChatAgent(
    name="Bob",
    system_prompt="You are a skeptical scientist. Respond with evidence-based reasoning. Keep replies concise.",
)


def run():
    message = "Is consciousness purely a product of physical processes?"
    print(f"\n[{agent_a.name}]: {message}")
    
    for i in range(ROUNDS):
        message = agent_b.reply(message)
        print(f"\n[{agent_b.name}]: {i + 1}.{message}")
        message = agent_a.reply(message)
        print(f"\n[{agent_a.name}]: {i + 1}.{message}")


if __name__ == "__main__":
    run()
