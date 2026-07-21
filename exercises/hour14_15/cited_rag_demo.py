knowledge = {
    "langchain":
        "LangChain is a framework for LLM applications.",

    "langgraph":
        "LangGraph is used for multi-step agent workflows.",

    "langsmith":
        "LangSmith provides tracing and debugging."
}

question = input("Ask a question: ").lower()

found = False

for keyword, answer in knowledge.items():

    if keyword in question:

        print("\nAnswer:")
        print(answer)

        print("\nSource:")
        print("knowledge_base.txt")

        found = True


if not found:

    print("\nNo relevant answer found.")