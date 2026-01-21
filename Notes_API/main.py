from fastapi import FastAPI
from Notes_API.app.database import engine, Base
from Notes_API.models import task


from Notes_API.routers.notes import router


Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(router=router)


@app.get("/")
async def root():
    return {"message": "Hello!"}