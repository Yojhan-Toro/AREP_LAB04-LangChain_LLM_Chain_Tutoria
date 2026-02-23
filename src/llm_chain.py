import os
from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage


load_dotenv()

def get_llm(model: str = "gemini-2.0-flash", temperature: float = 0.7):
    """Create and return a ChatGoogleGenerativeAI instance."""
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise ValueError("GOOGLE_API_KEY not found. Please set it in your .env file.")

    return ChatGoogleGenerativeAI(
        model=model,
        temperature=temperature,
        google_api_key=api_key
    )

def demo_direct_invocation(llm) -> None:
    """Demonstrate direct model invocation with a list of messages."""
    print("\n" + "="*60)
    print("DEMO 1: Direct Model Invocation")
    print("="*60)

    messages = [
        SystemMessage(content="You are a helpful assistant specialized in software architecture."),
        HumanMessage(content="What is SOLID in software design? Give a brief explanation."),
    ]

    response = llm.invoke(messages)
    print(f"\nResponse:\n{response.content}")

def demo_prompt_template(llm) -> None:
    """Demonstrate using ChatPromptTemplate with a chain."""
    print("\n" + "="*60)
    print("DEMO 2: Prompt Template + Chain")
    print("="*60)

    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are an expert professor in {subject}. Answer clearly and concisely."),
        ("human", "{question}")
    ])

    output_parser = StrOutputParser()
    chain = prompt | llm | output_parser

    result = chain.invoke({
        "subject": "Cloud Computing and Distributed Systems",
        "question": "Explain the CAP theorem in simple terms with a practical example."
    })

    print(f"\nChain Result:\n{result}")

def demo_sequential_chain(llm) -> None:
    """Demonstrate chaining two prompts sequentially."""
    print("\n" + "="*60)
    print("DEMO 3: Sequential Chain")
    print("="*60)

    output_parser = StrOutputParser()

    first_prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a software engineer. Explain concepts briefly."),
        ("human", "Explain what {concept} is in 2-3 sentences.")
    ])
    first_chain = first_prompt | llm | output_parser

    second_prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a Python expert. Write only code with minimal comments."),
        ("human", "Based on this concept:\n\n{explanation}\n\nWrite a simple Python example that illustrates it.")
    ])
    second_chain = second_prompt | llm | output_parser

    concept = "Dependency Injection"
    print(f"\nConcept: {concept}")

    explanation = first_chain.invoke({"concept": concept})
    print(f"\nStep 1 - Explanation:\n{explanation}")

    code_example = second_chain.invoke({"explanation": explanation})
    print(f"\nStep 2 - Code Example:\n{code_example}")

def demo_conversation(llm) -> None:
    """Demonstrate a simple multi-turn conversation."""
    print("\n" + "="*60)
    print("DEMO 4: Multi-turn Conversation")
    print("="*60)

    conversation_history = []

    questions = [
        "You are a helpful software architecture advisor. What are microservices?",
        "What are the main advantages over monolithic architecture?",
        "When should I NOT use microservices?"
    ]

    for i, question in enumerate(questions, 1):
        print(f"\nTurn {i} - User: {question}")
        conversation_history.append(HumanMessage(content=question))

        response = llm.invoke(conversation_history)
        answer = response.content
        conversation_history.append(AIMessage(content=answer))

        print(f"Assistant: {answer[:300]}{'...' if len(answer) > 300 else ''}")

if __name__ == "__main__":

    print("       AREP LAB 04 - LangChain LLM Chain Tutorial        ")
    print("              Powered by Google Gemini (Free)            ")


    llm = get_llm()

    demo_direct_invocation(llm)
    demo_prompt_template(llm)
    demo_sequential_chain(llm)
    demo_conversation(llm)

    print("\n" + "="*60)
    print("All demos completed successfully!")
    print("="*60)
