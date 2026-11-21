from fastapi import APIRouter
from src.api.chat_schema import ChatRequest, ChatResponse
from src.retriever.retriever import retriever  
from src.prompts.main_prompt import prompt_template
from src.llms.groq import llm

router = APIRouter()

@router.post("/chat")
def chat_api(chat_request: ChatRequest):
    # Retrieve documents based on the question
    retrieved_docs = retriever.invoke(chat_request.question)
    content = "\n".join([document.page_content for document in retrieved_docs])

    # Format the prompt with the retrieved content and the question
    formatted_prompt = prompt_template.format(context=content, question=chat_request.question)

    # Get the response from the language model
    response = llm.invoke(formatted_prompt)
    return ChatResponse(answer=response.content)