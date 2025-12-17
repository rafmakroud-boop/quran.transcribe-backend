from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Quran Transcriber backend online"}

@app.post("/transcribe")
def transcribe():
    # Qui metterai la logica di trascrizione
    return {"result": "demo"}