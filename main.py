from fastapi import FastAPI, HTTPException
from request_and_response import Request, Response
from procedure import summarize_text
from Logger_Config import logger
from Logger_Config.logger import logging
import uvicorn
import json

app = FastAPI()
logger.config_logger()


@app.get("/home")
def home():
    return "Summarize swedish text API. Send application/json: 'input':'your article' "


@app.post("/summarize/", response_model=Response)
def summarize(request_data: Request):
    try:
        logging.info("Summarize called. Run AI procedure.")
        result = summarize_text(request_data.input)
        logging.info(f"Returning result.")
        return Response(output=result)
    except Exception as e:
        error = HTTPException(status_code=500, detail=str(e))
        logging.warning(f"{error}")
        raise error


if __name__ == "__main__":

    logging.info("Application start up.")

    with open("config.json", "r") as f:
        config = json.load(f)

    host = config.get('host')
    port = config.get("port")

    logging.info(f"Hosting API on {host}:{port}")
    uvicorn.run(app, host=host, port=int(port))
