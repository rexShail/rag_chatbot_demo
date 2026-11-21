from langchain_core.prompts import ChatPromptTemplate

prompt_template = ChatPromptTemplate.from_template(
    "You are a Shailender Singh (rexShail) assistant. Use the following context to answer the question.\n\nContext:\n{context}\n\nQuestion: {question}\nAnswer:"
)   