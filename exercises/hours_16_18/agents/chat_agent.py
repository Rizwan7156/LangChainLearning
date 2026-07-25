"""
Hours 16-18

Chat Agent

✅ Agent
✅ Claude API
✅ LangChain
✅ LLM
"""

class ChatAgent:

    def __init__(self, llm):

        self.llm = llm

    def execute(self, question):

        prompt = f"""
        Answer the question clearly.

        Question:
        {question}
        """

        response = self.llm.invoke(
            prompt
        )

        return response.content