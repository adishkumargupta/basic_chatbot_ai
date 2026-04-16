from langgraph.graph import StateGraph
from typing import TypedDict
from dotenv import load_dotenv
import openai
import os

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), ".env"))

class State(TypedDict):
    prompt: str
    reply: str

openai_api_key = os.getenv("OPENAI_API_KEY")
if not openai_api_key:
    raise ValueError("OPENAI_API_KEY is not set in the environment")
openai.api_key = openai_api_key

MODEL_NAME = os.getenv("OPENAI_MODEL", "gpt-3.5-turbo")


def chatbot(state: State):
    user_prompt = state["prompt"]
    response = openai.chat.completions.create(
        model=MODEL_NAME,
        messages=[{"role": "user", "content": user_prompt}],
        temperature=0.7,
    )

    return {"reply": response.content.strip()}


graph = StateGraph(State)

graph.add_node("chatbot",chatbot)
graph.set_entry_point("chatbot")
graph.set_finish_point("chatbot")

workflow = graph.compile()