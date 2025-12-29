from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Pakistani AI Backend is running 🇵🇰"}

@app.post("/chat")
def chat(prompt: str):
    return {
        "reply": "Assalam-o-Alaikum! Pakistani AI abhi basic mode me hai 🙂"
    }
