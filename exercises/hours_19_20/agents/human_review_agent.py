"""
Hours 19-20

Human Review Agent

✅ Human Review Checkpoint
✅ Human Approval
✅ Human Rejection
"""

from tools.approval_tool import (
    approve_result
)

class HumanReviewAgent:

    def review(
        self,
        text,
        approved
    ):

        return approve_result(
            approved,
            text
        )