from sqlalchemy.orm import Session
from app.models import User, Movie
from app.schemas import UserCreate, MovieCreate

# CRUD User
def create_user(db: Session, user: UserCreate):
    db_user = User(username=user.username, email=user.email, password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()

# CRUD Movie
def create_movie(db: Session, movie: MovieCreate):
    db_movie = Movie(title=movie.title, description=movie.description, rating=movie.rating)
    db.add(db_movie)
    db.commit()
    db.refresh(db_movie)
    return db_movie

def list_movies(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Movie).offset(skip).limit(limit).all()
