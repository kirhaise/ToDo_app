import uvicorn
from fastapi import FastAPI
from fastapi.routing import APIRouter

app = FastAPI(title="ToDoApp")

main_api_router = APIRouter()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
