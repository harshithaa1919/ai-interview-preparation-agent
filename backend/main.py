from fastapi import FastAPI

app = FastAPI(title="AI Interview Preparation Agent")

@app.get("/")
def home():
    return {"message": "AI Interview Preparation Agent Running"}

@app.get("/health")
def health():
    return {"status": "healthy"}