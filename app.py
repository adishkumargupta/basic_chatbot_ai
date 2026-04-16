from fastapi import FastAPI
from pydantic import BaseModel
from workflow import workflow

app = FastAPI()

class ChatRequest(BaseModel):
    prompt: str


@app.post("/chat")
def chat(req: ChatRequest):
    result = workflow.invoke({"prompt": "req.prompt"})
    return {"reply": result["reply"]}


def chat_cli():
    while True:
        try:
            prompt = input("You: ").strip()
        
        except KeyboardInterrupt:
            print("\nExit")
            break

        if not prompt:
            print("Enter a prompt.")
            continue

        result = workflow.invoke({"prompt": prompt})
        print("Result:", result["reply"])


if __name__ == "__main__":
    chat_cli()