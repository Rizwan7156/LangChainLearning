"""
Hours 16-18

Routing Tool

✅ Tool
✅ Conditional Routing
"""

def route_question(question):

    q = question.lower()

    rag_keywords = [
        "rag",
        "langgraph",
        "langchain",
        "embedding",
        "retriever",
        "vector"
    ]

    if any(
        keyword in q
        for keyword in rag_keywords
    ):

        return "rag"

    return "chat"