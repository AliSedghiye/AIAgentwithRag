from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

from vector import retriver

model = OllamaLLM(model="phi3")

template = """
You are an expert in answering questions about a pizza restaurant.

Here are some relevant reviews: {reviews}

Here is the question you need to answer: {question}
"""

prompts = ChatPromptTemplate.from_template(template)
chain = prompts | model


while True:
    print("\n\n------------------------------------------------------------")
    question = input("Please enter your question (q to quit): ")
    print("\n\n------------------------------------------------------------")
    if question.lower() == "q":
        break

    reviews = retriver.invoke(question)
    result = chain.invoke({"reviews": reviews, "question": question})
    print(result)