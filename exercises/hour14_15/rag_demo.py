from langchain_core.documents import Document

# Small Knowledge Base
docs = [
    Document(
        page_content="LangChain is a framework for developing applications powered by language models."
    ),
    Document(
        page_content="LangGraph is used for building stateful multi-step agent workflows."
    ),
    Document(
        page_content="LangSmith provides tracing, debugging and monitoring for LLM applications."
    ),
]

question = input("Ask a question: ").lower()

found = False

for doc in docs:

    content = doc.page_content.lower()

    if "langchain" in question and "langchain" in content:

        print("\nAnswer Found:")
        print(doc.page_content)
        found = True

    elif "langgraph" in question and "langgraph" in content:

        print("\nAnswer Found:")
        print(doc.page_content)
        found = True

    elif "langsmith" in question and "langsmith" in content:

        print("\nAnswer Found:")
        print(doc.page_content)
        found = True


if not found:

    print("\nNo relevant answer found.")