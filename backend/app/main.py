# Nexa AI Backend - Main Application

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes import users
from app.routes import diagnostic
from app.routes import paths
from app.routes import chat


app = FastAPI(
    title="Nexa AI API",
    description="API backend pour la plateforme intelligente Nexa AI",
    version="1.0.0"
)


# Configuration CORS

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Routes principales

app.include_router(
    users.router,
    prefix="/api/users",
    tags=["Users"]
)

app.include_router(
    diagnostic.router,
    prefix="/api/diagnostic",
    tags=["Diagnostic"]
)

app.include_router(
    paths.router,
    prefix="/api/paths",
    tags=["Learning Paths"]
)

app.include_router(
    chat.router,
    prefix="/api/chat",
    tags=["AI Mentor"]
)


@app.get("/")
def root():
    return {
        "project": "Nexa AI",
        "message": "API opérationnelle"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }
