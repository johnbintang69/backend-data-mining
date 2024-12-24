from fastapi import FastAPI
from app.routes import auth, movies
from app.database import Base, engine

# Inisialisasi database
Base.metadata.create_all(bind=engine)

# Inisialisasi aplikasi FastAPI
app = FastAPI()

# Include router
app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(movies.router, prefix="/movies", tags=["movies"])
