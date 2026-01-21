from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy import select
from sqlalchemy.orm import Session

from Notes_API.schemas import TaskCreate, TaskResponse, TaskUpdate
from Notes_API.app.database import get_db
from Notes_API.models.task import Task


router = APIRouter(prefix="/notes", 
                   tags=["Notes"]
                )

   


@router.post("/", response_model=TaskResponse)
async def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    db_task = Task(**task.model_dump())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task


@router.get("/", response_model=list[TaskResponse])
async def get_tasks(db: Session = Depends(get_db)):
    tasks = select(Task)
    task = db.scalars(tasks).all()

    return task


@router.get("/{id}", response_model=TaskResponse)
async def get_task_by_id(id: int, db: Session = Depends(get_db)):
    tasks = select(Task).where(Task.id == id)
    task = db.scalars(tasks).one_or_none()
    
    if task is None:
        raise HTTPException(status_code=404, detail="Note not found")
        
    return task


@router.delete("/{id}", response_model=TaskResponse)
async def delete_task_by_id(id: int, db: Session = Depends(get_db)):
    task = db.get(Task, id)
    if not task:
        raise HTTPException(status_code=404, detail="Note not found")
    db.delete(task)
    db.commit()

    return task


@router.patch("/{id}", response_model=TaskResponse)
async def update_task_by_id(id: int, task_update: TaskUpdate, db:Session = Depends(get_db)):
    task = db.get(Task, id)
    if not task:
        raise HTTPException(status_code=404, detail="Note not found")
    
    data = task_update.model_dump(exclude_unset=True)
    if not data:
        raise HTTPException(status_code=400, detail="No data to update")

    for key, value in data.items():
        setattr(task, key, value)

    db.commit()

    return task