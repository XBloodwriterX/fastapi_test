from fastapi import FastAPI
from contextlib import asynccontextmanager
import uvicorn

from database import create_tables, delete_tables
from router import task_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print("Database cleaned")
    await create_tables()
    print("Database created")
    yield
    print("Shutting down")

app = FastAPI(lifespan=lifespan)
app.include_router(task_router)



if __name__ == "__main__":
    uvicorn.run("main:app", port=7000, reload=True)