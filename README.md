## This project implements a modular Retrieval-Augmented Generation (RAG) pipeline for a Q&A chatbot designed specifically for answering medical-related queries. The system leverages Llama2 for language generation and integrates a retrieval mechanism for enhanced contextual accuracy.

## Features
## Retrieval-Augmented Generation (RAG): Combines retrieval from a knowledge base with generative responses.
## Modular Design: All components are modularized for clarity, scalability, and maintainability.
## Custom Embeddings: Generates embeddings for medical documents for efficient search.
## Web Interface: Provides a user-friendly web interface for interaction.
## Open Source: Ready-to-extend framework for custom use cases.

## Folder Structure
## This project follows a modular approach for cleaner and more maintainable code, as evident in the directory structure:
.
├── data                    # Stores input documents (medical texts or PDFs)
├── model                   # Contains pre-trained and fine-tuned models
├── src                     # Core modules of the application
│   ├── app.py              # Main application logic
│   ├── helper.py           # Utility functions (e.g., file handling, data preprocessing)
│   ├── executor.py         # Executes RAG pipeline (retrieval + generation)
│   ├── prompt.py           # Defines prompt templates for Llama2
├── static                  # Static files (CSS/JS for web interface)
├── templates               # HTML templates for Flask web app
├── trails.ipynb            # Jupyter notebook for prototyping and experiments
├── requirements.txt        # Python dependencies
├── .env                    # Environment variables (e.g., API keys, secrets)
└── README.md               # Project documentation

## Workflow
## 1. Data Ingestion: Loads and preprocesses medical documents.
## 2. Embedding Generation: Converts documents into dense vector representations for retrieval.
## 3. RAG Pipeline:
##  - Retrieval: Fetches relevant documents using embeddings.
##  - Generation: Llama2 generates contextually accurate responses.
## 4. Web Interface: Users can interact with the chatbot via a web-based UI.


## Modular Design
## The codebase is designed to ensure modularity, with separate files for each component:

## helper.py:
## - Contains utility functions for data loading and preprocessing.
## - Handles embedding generation and storage.

## executor.py:
## - Combines retrieval and generation steps.
## - Implements the RAG pipeline.

## prompt.py:
## - Defines structured prompts for Llama2 to ensure consistent and accurate responses.

## app.py:
## - Connects all components to create a Flask-based web application

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
