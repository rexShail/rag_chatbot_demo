from src.retriever.retriever import retrieved_docs, question
from src.prompts.main_prompt import prompt_template
from src.llms.groq import llm

content = "\n".join([document.page_content for document  in retrieved_docs])
formatted_prompt = prompt_template.format(context=content, question=question)
response = llm.invoke(formatted_prompt)
print(f"Response: {response.content}")  

