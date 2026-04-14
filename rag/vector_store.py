from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

# Path where the persistent vector database will be stored
VECTOR_DB_PATH = "vector_db"

# Embedding model
embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Persistent vector store
vector_store = Chroma(
    persist_directory=VECTOR_DB_PATH,
    embedding_function=embedding_model
)