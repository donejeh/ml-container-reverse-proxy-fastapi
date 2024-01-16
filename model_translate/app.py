from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Response to Translated"}

