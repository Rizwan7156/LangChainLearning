"""
Hours 19-20

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

        response = self.llm.invoke(
            question
        )

        return response.content