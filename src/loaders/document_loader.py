from langchain_community.document_loaders import (
    PyPDFLoader,
    TextLoader,
    WebBaseLoader,
    Docx2txtLoader,
)
from langchain_core.documents import Document
from typing import List
import os


def load_documents(source: str) -> List[Document]:
    """
    Loads documents from a given source (file path or URL).

    Args:
        source: A file path or a URL.

    Returns:
        A list of Document objects.
    """
    if source.startswith("http://") or source.startswith("https://"):
        print(f"Loading web page: {source}")
        loader = WebBaseLoader(web_paths=(source,))
        return loader.load()

    if not os.path.exists(source):
        raise FileNotFoundError(f"The source '{source}' does not exist.")

    if os.path.isdir(source):
        # We can extend this later to load all files in a directory
        raise NotImplementedError("Loading from a directory is not yet implemented.")

    _, extension = os.path.splitext(source)
    extension = extension.lower()

    print(f"Loading file: {source} with extension {extension}")

    if extension == ".pdf":
        loader = PyPDFLoader(source)
    elif extension == ".txt":
        loader = TextLoader(source)
    elif extension == ".docx":
        loader = Docx2txtLoader(source)
    else:
        raise ValueError(f"Unsupported file extension: '{extension}'")

    return loader.load()
