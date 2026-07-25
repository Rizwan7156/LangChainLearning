"""
Hours 16-18

Checkpoint Tool

✅ Checkpointer
✅ Resume State
"""

from langgraph.checkpoint.memory import MemorySaver


def get_memory_checkpointer():

    return MemorySaver()