from fastapi import FastAPI
import uvicorn

app = FastAPI(
    title="Automated Multi-Source RAG Assistant",
    description="An API for a RAG assistant that can process data from multiple sources.",
    version="0.1.0",
)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Automated Multi-Source RAG Assistant API"}

@app.get("/health")
def health_check():
    return {"status": "ok"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
