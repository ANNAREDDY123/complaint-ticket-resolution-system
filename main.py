from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database import (
    Base,
    engine
)

from models.user import User
from models.agent import Agent
from models.complaint import Complaint
from models.resolution import Resolution

from routes.auth import router as auth_router
from routes.complaints import router as complaint_router
from routes.agents import router as agent_router
from routes.reports import router as report_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Complaint & Ticket Resolution System"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(auth_router)
app.include_router(complaint_router)
app.include_router(agent_router)
app.include_router(report_router)


@app.get("/")
def home():

    return {
        "message":
        "Complaint & Ticket Resolution System"
    }
