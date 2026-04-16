from fastapi import FastAPI
from pydantic import BaseModel
from workflow import workflow

app = FastAPI()

class ChatRequest(BaseModel):
    prompt: str

@app.get("/")
def home():
    return {"message": "Please provide the information about openai"}

@app.post("/chat")
def chat(req: ChatRequest):
    result = workflow.invoke({"prompt": "req.prompt"})
    return {"reply": result["reply"]}


def chat_cli():
    print("Start chatting with OpenAI. Type your prompt and press Enter. Ctrl+C to exit.")
    while True:
        try:
            prompt = input("You: ").strip()
        except KeyboardInterrupt:
            print("\nExiting chat.")
            break

        if not prompt:
            print("Enter a prompt.")
            continue

        result = workflow.invoke({"prompt": prompt})
        print("Bot:", result["reply"])


if __name__ == "__main__":
    chat_cli()