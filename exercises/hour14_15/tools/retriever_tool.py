"""
Hours 14-15

Retriever Tool

✅ Retriever
✅ Context Retrieval
"""

def create_retriever(
    vectorstore
):

    retriever = (
        vectorstore.as_retriever(
            search_kwargs={
                "k": 3
            }
        )
    )

    return retriever