from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

from rag.vector_store import vector_store

def ingest_doc():
    
    loader = PyPDFLoader(r'C:\Users\VilasTade\OneDrive - IBM\Projects\Practice Projects\A2A blog writer\doc\book2.pdf')
    
    documents= loader.load()
    
    splitter = RecursiveCharacterTextSplitter(
        chunk_size = 1000,
        chunk_overlap = 100
    )
    
    chunks = splitter.split_documents(documents)
    print(len(chunks))
    for d in chunks:
        d.page_content = d.page_content.encode("utf-8", "ignore").decode("utf-8", "ignore")
        
    vector_store.add_documents(chunks)

    print(vector_store._collection.count())
    vector_store.persist()

    print("Documents ingested successfully")
    
    
if __name__ == 'main':
    ingest_doc()