from fastapi import APIRouter, Depends
from typing import Annotated

from repository import TaskRepository
from schemas import STaskAdd, STask, STaskId

task_router = APIRouter(
    prefix="/tasks",
    tags=["tasks"],
)

@task_router.post("")
async def add_task(
    task: Annotated[STaskAdd, Depends()]
) -> STaskId:
    task_id = await TaskRepository.add_one(task)
    return {"ok": True, "task_id": task_id}


@task_router.get("")
async def get_tasks() -> list[STask]:
    tasks = await TaskRepository.find_all()
    return tasks