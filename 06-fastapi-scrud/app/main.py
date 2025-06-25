from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from typing import List

from .models import Base, Cuisine, CuisineCreate, CuisineUpdate, CuisineRead

DATABASE_URL = "sqlite:///./cuisines.db"

engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)


@app.post("/cuisines/", response_model=CuisineRead)
def create_cuisine(cuisine: CuisineCreate, db: Session = Depends(get_db)):
    db_cuisine = Cuisine(**cuisine.dict())
    db.add(db_cuisine)
    db.commit()
    db.refresh(db_cuisine)
    return db_cuisine


@app.get("/cuisines/", response_model=List[CuisineRead])
def read_cuisines(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    cuisines = db.query(Cuisine).offset(skip).limit(limit).all()
    return cuisines


@app.get("/cuisines/{cuisine_id}", response_model=CuisineRead)
def read_cuisine(cuisine_id: int, db: Session = Depends(get_db)):
    cuisine = db.query(Cuisine).filter(Cuisine.id == cuisine_id).first()
    if cuisine is None:
        raise HTTPException(status_code=404, detail="Cuisine not found")
    return cuisine


@app.put("/cuisines/{cuisine_id}", response_model=CuisineRead)
def update_cuisine(
    cuisine_id: int,
    cuisine: CuisineUpdate,
    db: Session = Depends(get_db),
):
    db_cuisine = db.query(Cuisine).filter(Cuisine.id == cuisine_id).first()
    if db_cuisine is None:
        raise HTTPException(status_code=404, detail="Cuisine not found")

    update_data = cuisine.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_cuisine, key, value)
    db.commit()
    db.refresh(db_cuisine)
    return db_cuisine


@app.delete("/cuisines/{cuisine_id}")
def delete_cuisine(cuisine_id: int, db: Session = Depends(get_db)):
    db_cuisine = db.query(Cuisine).filter(Cuisine.id == cuisine_id).first()
    if db_cuisine is None:
        raise HTTPException(status_code=404, detail="Cuisine not found")
    db.delete(db_cuisine)
    db.commit()
    return {"ok": True}

