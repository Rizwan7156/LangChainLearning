"""
Hours 19-20

Approval Tool

✅ Human Review Checkpoint
✅ Human Approval
✅ Human Rejection
"""

def approve_result(
    approved,
    text
):

    if approved:

        return {
            "approved": True,
            "comment":
            "Approved by Human Reviewer",
            "result": text
        }

    return {
        "approved": False,
        "comment":
        "Rejected by Human Reviewer",
        "result": text
    }