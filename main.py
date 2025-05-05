from datetime import datetime

import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_time():
    """
    Returns the current server time in ISO format.
    """
    return {"current_time": datetime.now().isoformat()}


if __name__ == "__main__":
    # Launch with uvicorn on localhost:8000
    uvicorn.run("main:app", host="127.0.0.1", port=8000)
