
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

load_dotenv()


def run_chatbot():

    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY not found. Check your .env file.")

    llm = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0.7,
        openai_api_key=api_key
    )


    print("          AREP LAB 04 - Interactive Chatbot             ")
    print("             Powered by LangChain + OpenAI              ")
  
    print("\nType your message and press Enter. Type 'exit' or 'quit' to stop.\n")

    system_prompt = input("Enter a system prompt (or press Enter for default): ").strip()
    if not system_prompt:
        system_prompt = "You are a helpful software engineering assistant with expertise in distributed systems, cloud computing, and modern software architecture."

    conversation_history = [SystemMessage(content=system_prompt)]
    print(f"\nSystem prompt set. Starting conversation...\n{'─'*60}\n")

    while True:
        user_input = input("You: ").strip()

        if not user_input:
            continue

        if user_input.lower() in ["exit", "quit", "bye"]:
            print("\nGoodbye! Thanks for using AREP LAB 04 Chatbot.")
            break

        if user_input.lower() == "clear":
            conversation_history = [conversation_history[0]]
            print("Conversation history cleared.\n")
            continue

        if user_input.lower() == "history":
            print("\n--- Conversation History ---")
            for msg in conversation_history[1:]:
                role = "You" if isinstance(msg, HumanMessage) else "Assistant"
                print(f"{role}: {msg.content[:100]}...")
            print("----------------------------\n")
            continue

        conversation_history.append(HumanMessage(content=user_input))

        try:
            response = llm.invoke(conversation_history)
            assistant_message = response.content
            conversation_history.append(AIMessage(content=assistant_message))

            print(f"\nAssistant: {assistant_message}\n{'─'*60}\n")

        except Exception as e:
            print(f"\nError communicating with OpenAI: {e}\n")
            conversation_history.pop() 


if __name__ == "__main__":
    run_chatbot()
