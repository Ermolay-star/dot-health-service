from fastapi import FastAPI

app = FastAPI(title="Health Service")


@app.get("/health")
def health_check():
    return {"status": "ok"}