from pydantic import BaseModel
from typing import Optional

# User schema
class UserBase(BaseModel):
    username: str
    email: str

class UserCreate(UserBase):
    password: str

class UserOut(UserBase):
    id: int

    class Config:
        orm_mode = True

# Movie schema
class MovieBase(BaseModel):
    title: str
    description: str
    rating: float

class MovieCreate(MovieBase):
    pass

class MovieOut(MovieBase):
    id: int

    class Config:
        orm_mode = True
