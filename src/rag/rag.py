from retrive_data import load_data, split_data
from embedding_data import embed_text, setup_chroma_db, query_chuncks


def main():
    # Load and split documents
    collection = setup_chroma_db()
    exist_ids = collection.get()['ids']
    
    documents = load_data()

    texts = split_data(documents)

    embedding = embed_text(texts)
    print(f"First text chunk embedding: {embedding}")

    for i, text in enumerate(texts):
        if f"doc_{i}" in exist_ids:
            print(f"Document doc_{i} already exists in the database. Skipping insertion.")
            continue
        collection.upsert(
            ids=[f"doc_{i}"],
            documents=[text.page_content],
            embeddings=[embedding[i]]
        )
    results = query_chuncks("What is ?", collection)
    print(f"Query results: {results}")
    
if __name__ == "__main__":
    main()