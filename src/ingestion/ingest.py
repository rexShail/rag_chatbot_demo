
from langchain_community.document_loaders import TextLoader, DirectoryLoader, PyPDFLoader

loader = DirectoryLoader("data", 
                         glob="**/*.txt", 
                         loader_cls=TextLoader)

documents = loader.load()
