"""
Hours 14-15

Vector Store Tool

✅ Embeddings
✅ Vector Store
"""

from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import FakeEmbeddings


def build_vectorstore(chunks):

    embeddings = FakeEmbeddings(
        size=768
    )

    vectorstore = FAISS.from_documents(
        chunks,
        embeddings
    )

    return vectorstore