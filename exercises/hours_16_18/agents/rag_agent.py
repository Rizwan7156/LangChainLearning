"""
Hours 16-18

RAG Agent

✅ Agent
✅ Retriever
✅ Grounded Generation
"""

class RagAgent:

    def __init__(
        self,
        llm,
        retriever
    ):

        self.llm = llm
        self.retriever = retriever

    def execute(self, question):

        docs = self.retriever.invoke(
            question
        )

        context = "\n".join(
            [
                d.page_content
                for d in docs
            ]
        )

        prompt = f"""
        Context:
        {context}

        Question:
        {question}

        Answer only from the context.
        """

        response = self.llm.invoke(
            prompt
        )

        return response.content