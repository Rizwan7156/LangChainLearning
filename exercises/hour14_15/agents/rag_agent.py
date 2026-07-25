"""
Hours 14-15

RAG Agent

✅ Agent
✅ LangChain
✅ Claude API
✅ Grounded Generation
"""

class RAGAgent:

    def __init__(self, llm, retriever):

        self.llm = llm
        self.retriever = retriever

    def execute(self, question):

        docs = self.retriever.invoke(
            question
        )

        context = "\n\n".join(
            [
                doc.page_content
                for doc in docs
            ]
        )

        prompt = f"""
You are a RAG assistant.

Answer ONLY from the provided context.

Context:
{context}

Question:
{question}

Provide:

1. Answer
2. Source Snippet
"""

        response = self.llm.invoke(
            prompt
        )

        return {
            "answer": response.content,
            "source_docs": docs
        }