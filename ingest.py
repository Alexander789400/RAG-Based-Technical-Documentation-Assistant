import os

from langchain_community.document_loaders import TextLoader

from langchain_text_splitters import RecursiveCharacterTextSplitter

from app.vectorstore.db import vectordb


DOCS_PATH = "app/data/docs"


def ingest_documents():

    all_documents = []

    for file in os.listdir(DOCS_PATH):

        if file.endswith(".md") or file.endswith(".txt"):

            path = os.path.join(DOCS_PATH, file)

            loader = TextLoader(path)

            documents = loader.load()

            for doc in documents:
                doc.metadata["source"] = file

            all_documents.extend(documents)

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    chunks = splitter.split_documents(all_documents)

    vectordb.add_documents(chunks)

    return len(chunks)