from fastapi import FastAPI, HTTPException
import uvicorn
from .routers import files

app = FastAPI(debug=True)

app.include_router(files.router)

@app.get("/")
async def root():
    return {"message": "Hello"}