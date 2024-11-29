# Medical Chatbot with Llama 2, Pinecone, LangChain, and HuggingFace Embeddings
## This project demonstrates how to build a retrieval-augmented generation (RAG) model using LangChain, Pinecone, and HuggingFace Embeddings, with ## Llama 2 for generating chatbot responses. The aim is to develop a medical chatbot capable of retrieving relevant information from PDF documents ## and answering user queries.

## Steps to run the project:


### 1. Create and activate Virtual Environment
### 2. Install the required libraries
### 3. Load PDF Data using PyPDF Loader
### 4. Split the data into chunks using 

## Overview

### This repository provides a walkthrough for building a chatbot with the following components:
### Document Loading: Extracts content from a directory of PDFs.
### Text Splitting: Prepares the text for embeddings.
### Embeddings: Generates dense vector representations using HuggingFace models.
### Vector Indexing: Stores and queries data efficiently with Pinecone.
### Language Model: Llama 2, integrated through LangChain and Transformers.

### Resources:
- [LLaMA](https://github.com/meta-llama)
- [Quantized Model](https://huggingface.co/models?search=llama%202%20ggml)
- [Model](https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/tree/main)
- [Llama2-13B](https://huggingface.co/TheBloke/CodeUp-Llama-2-13B-Chat-HF-GGML)
- [Langchain](https://github.com/langchain-ai/langchain)
- [Langchain-Docs](https://python.langchain.com/docs/introduction/)
- [Embedding Model](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2)