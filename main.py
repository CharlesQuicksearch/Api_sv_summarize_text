from fastapi import FastAPI, HTTPException


app = FastAPI()

@app.get("/home")
def home():
    return "Summarize swedish text API. Send application/json: 'input':'your article' "

@app.post("/summarize/")
def summarize():
    try:
        return None
    except Exception as e:
       raise HTTPException(status_code=500, detail=str(e))
