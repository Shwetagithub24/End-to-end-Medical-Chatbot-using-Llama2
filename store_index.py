from src.helper import load_pdf, text_split,download_hugging_face_embeddings
from langchain.vectorstores import Pinecone
from pinecone import Pinecone, ServerlessSpec
import pinecone
from dotenv import load_dotenv
import os

load_dotenv()

PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')

# Extract pdf

extracted_data = load_pdf("data/")

# Split text

text_chunks = text_split(extracted_data)

#download embeddings
embeddings = download_hugging_face_embeddings()
print(type(embeddings))

PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')
# Initialize Pinecone
pc = Pinecone(api_key = PINECONE_API_KEY)

# Create index
import pinecone
from pinecone import Pinecone, ServerlessSpec


index_name = "medicalchatbot2"

pc.create_index(
    name=index_name,
    dimension=384, # Replace with your model dimensions
    metric="cosine", # Replace with your model metric
    spec=ServerlessSpec(
        cloud="aws",
        region="us-east-1"
    ) 
)

index = pc.Index('medicalchatbot2')

# Upsert data
#embed each chunk and upsert embeddings into Pinecone index
from langchain_pinecone import PineconeVectorStore

docsearch = PineconeVectorStore.from_documents(
    documents=text_chunks,
    index_name = index_name,
    embedding=embeddings
)


'''
id_counter = 0
vectors_to_upsert = []


# Generate embeddings and prepare data for upsert
for i, doc in enumerate(text_chunks):
    text_chunk = doc.page_content  # Extract the chunk of text
    vector = embeddings.embed_documents([text_chunk])[0]  # Generate embedding
    vectors_to_upsert.append({
        "id": str(id_counter),
        "values": vector,
        "metadata": {"text": text_chunk}
    })
    id_counter += 1
    

# Batch size for upserts (adjust to fit under 4 MB per request)
BATCH_SIZE = 100

# Upsert data in batches
for i in range(0, len(vectors_to_upsert), BATCH_SIZE):
    batch = vectors_to_upsert[i:i + BATCH_SIZE]
    index.upsert(vectors=batch)

print(f"Successfully upserted {len(vectors_to_upsert)} vectors to Pinecone {index}.")
'''

# load existing index
from langchain_pinecone import PineconeVectorStore

docsearch = PineconeVectorStore.from_existing_index(
    index_name = index_name,
    embedding=embeddings
)
