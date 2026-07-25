"""
Hours 19-20

Routing Tool

✅ Tool
✅ Conditional Routing
✅ Supervisor Pattern

Purpose:
Determine which agent should
handle the incoming request.
"""

def route_request(question):

    q = question.lower()

    # ==========================================
    # EVALUATION ROUTE
    # ==========================================

    if (
        "evaluation" in q
        or "run evaluation" in q
        or "evaluate" in q
    ):
        return "evaluation"

    # ==========================================
    # RAG ROUTE
    # ==========================================

    if any(
        word in q
        for word in [
            "rag",
            "langgraph",
            "langchain",
            "embedding",
            "embeddings",
            "retriever",
            "vector",
            "faiss"
        ]
    ):
        return "rag"

    # ==========================================
    # DEFAULT ROUTE
    # ==========================================

    return "chat"