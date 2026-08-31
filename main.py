from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"status": "OSINT backend running", "message": "DIYOTOYE OSINT online"}

@app.get("/ping")
def ping():
    return {"pong": True}

@app.get("/osint/user/{username}")
def osint_user(username: str):
    return {"user": username, "status": "lookup-ready"}
