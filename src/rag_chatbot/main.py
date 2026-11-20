from langchain_community.document_loaders import TextLoader

loader = TextLoader("data/data.txt")
docs = loader.load()

print(docs)