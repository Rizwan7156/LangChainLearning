"""
Hours 19-20

Supervisor Agent

✅ Agent
✅ Multi-Agent Routing
✅ LangGraph Supervisor Pattern
"""

from tools.routing_tool import route_request


class SupervisorAgent:

    def route(self, question):

        return route_request(
            question
        )