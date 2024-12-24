from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.crud import create_movie, list_movies
from app.schemas import MovieCreate
from app.database import get_db

router = APIRouter()

# Endpoints
@router.post("/")
def add_movie(movie: MovieCreate, db: Session = Depends(get_db)):
    return create_movie(db=db, movie=movie)

@router.get("/")
def get_movies(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return list_movies(db=db, skip=skip, limit=limit)
