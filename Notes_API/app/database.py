from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from pathlib import Path


class Base(DeclarativeBase):
    pass



BASE_DIR = Path(__file__).resolve().parent


data_dir = BASE_DIR / "storage"
data_dir.mkdir(exist_ok=True)

file_path = data_dir / "tasks.db"


engine = create_engine(f"sqlite:///{file_path}", echo=False)

SessionLocal = sessionmaker(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()