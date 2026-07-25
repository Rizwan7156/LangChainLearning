"""
Hours 16-18

Supervisor Agent

✅ Agent
✅ Multi-Agent Pattern
✅ LangGraph Routing
"""

from tools.routing_tool import route_question


class SupervisorAgent:

    def route(self, question):

        return route_question(
            question
        )