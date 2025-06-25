from sqlalchemy import Column, Integer, String, JSON
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel
from typing import Optional

Base = declarative_base()


class Cuisine(Base):
    __tablename__ = "cuisines"

    id = Column(Integer, primary_key=True, index=True)
    nom = Column(String, index=True)
    temps = Column(Integer)
    ingredients = Column(JSON)


class CuisineCreate(BaseModel):
    nom: str
    temps: int
    ingredients: dict


class CuisineUpdate(BaseModel):
    nom: Optional[str] = None
    temps: Optional[int] = None
    ingredients: Optional[dict] = None


class CuisineRead(BaseModel):
    id: int
    nom: str
    temps: int
    ingredients: dict

    class Config:
        orm_mode = True
