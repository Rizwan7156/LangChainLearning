from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import FakeEmbeddings
from langchain_community.vectorstores import FAISS


# ==========================================
# STEP 1 - LOAD DOCUMENT
# ==========================================

loader = TextLoader(
    "exercises/hour14_15/knowledge_base.txt"
)

docs = loader.load()

print("\n=== STEP 1 : LOADER ===")
print("Loaded Documents:", len(docs))


# ==========================================
# STEP 2 - SPLIT DOCUMENT
# ==========================================

splitter = RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=20
)

chunks = splitter.split_documents(docs)

print("\n=== STEP 2 : TEXT SPLITTING ===")
print("Chunks Created:", len(chunks))

print("\n=== CHUNK DETAILS ===")

for i, chunk in enumerate(chunks, start=1):

    print(f"\nChunk {i}")
    print("-" * 40)
    print(chunk.page_content)

# ==========================================
# STEP 3 - CREATE EMBEDDINGS
# ==========================================

embeddings = FakeEmbeddings(size=10)
print("\n=== STEP 3A : SAMPLE EMBEDDING ===")

sample_vector = embeddings.embed_query(
    "LangGraph"
)

print("Embedding Vector Length:",
      len(sample_vector))

print("\nFirst 5 Numbers:")

for value in sample_vector[:5]:
    print(round(value, 3))

print("\n=== STEP 3 : EMBEDDINGS ===")
print("Embeddings Created Successfully")


# ==========================================
# STEP 4 - CREATE VECTOR STORE
# ==========================================

vectorstore = FAISS.from_documents(
    chunks,
    embeddings
)
print("\n=== STEP 4A : VECTOR STORE CONTENT ===")

for i, chunk in enumerate(chunks, start=1):

    print(f"\nChunk {i}")
    print("-" * 40)

    print(chunk.page_content)

    vector = embeddings.embed_query(
        chunk.page_content
    )

    print("\nVector Length:",
          len(vector))

    print("First 5 Values:",
          [round(v, 3)
           for v in vector[:5]])
    
print("\n=== STEP 4 : VECTOR STORE ===")
print("FAISS Vector Store Created")


# ==========================================
# STEP 5 - CREATE RETRIEVER
# ==========================================

retriever = vectorstore.as_retriever()

print("\n=== STEP 5 : RETRIEVER ===")
print("Retriever Created")


# ==========================================
# STEP 6 - QUESTION ANSWERING
# ==========================================

question = input(
    "\nAsk a question: "
).strip().lower()

results = retriever.invoke(question)

print("\n=== STEP 6 : RETRIEVED DOCUMENTS ===")

found = False

for index, doc in enumerate(results, start=1):

    content = doc.page_content.strip().lower()

    if "langchain" in question and "langchain" in content:

        print(f"\nResult {index}")
        print("-" * 40)
        print(doc.page_content)
        found = True

    elif "langgraph" in question and "langgraph" in content:

        print(f"\nResult {index}")
        print("-" * 40)
        print(doc.page_content)
        found = True

    elif "langsmith" in question and "langsmith" in content:

        print(f"\nResult {index}")
        print("-" * 40)
        print(doc.page_content)
        found = True

    elif "rag" in question and "rag" in content:

        print(f"\nResult {index}")
        print("-" * 40)
        print(doc.page_content)
        found = True

    elif "vector" in question and "vector" in content:

        print(f"\nResult {index}")
        print("-" * 40)
        print(doc.page_content)
        found = True


if not found:

    print("\nNo relevant answer found.")

print("\nSource:")
print("knowledge_base.txt")