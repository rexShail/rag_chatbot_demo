from langchain_community.document_loaders import TextLoader, PyPDFLoader

loader = PyPDFLoader("data/data.pdf")
docs = loader.load()

print(docs)