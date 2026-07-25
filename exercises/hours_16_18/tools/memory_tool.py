"""
Hours 16-18

Memory Tool

✅ State Memory
✅ Resume Behaviour
"""

memory_store = {}


def save_state(
    session_id,
    data
):

    memory_store[
        session_id
    ] = data


def load_state(
    session_id
):

    return memory_store.get(
        session_id,
        {}
    )