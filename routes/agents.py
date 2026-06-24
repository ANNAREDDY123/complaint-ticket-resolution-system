from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    BackgroundTasks
)

from sqlalchemy.orm import Session

from database import SessionLocal

from models.agent import Agent
from models.complaint import Complaint
from models.resolution import Resolution

from schemas.agent import AgentCreate
from schemas.resolution import ResolutionCreate

router = APIRouter(
    tags=["Agents & Tickets"]
)


def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


def send_assignment_email():

    print("Assignment email sent")


@router.post("/agents")
def create_agent(
    agent: AgentCreate,
    db: Session = Depends(get_db)
):

    new_agent = Agent(
        name=agent.name,
        email=agent.email,
        department=agent.department
    )

    db.add(new_agent)

    db.commit()

    db.refresh(new_agent)

    return new_agent


@router.get("/agents")
def get_agents(
    db: Session = Depends(get_db)
):

    return db.query(Agent).all()


@router.post("/tickets/{ticket_id}/assign/{agent_id}")
def assign_ticket(
    ticket_id: int,
    agent_id: int,
    background_tasks: BackgroundTasks,
    db: Session = Depends(get_db)
):

    ticket = db.query(Complaint).filter(
        Complaint.id == ticket_id
    ).first()

    if not ticket:

        raise HTTPException(
            status_code=404,
            detail="Ticket not found"
        )

    if ticket.status == "Closed":

        raise HTTPException(
            status_code=400,
            detail="Closed ticket cannot be assigned"
        )

    agent = db.query(Agent).filter(
        Agent.id == agent_id
    ).first()

    if not agent:

        raise HTTPException(
            status_code=404,
            detail="Agent not found"
        )

    ticket.agent_id = agent_id

    ticket.status = "In Progress"

    db.commit()

    background_tasks.add_task(
        send_assignment_email
    )

    return {
        "message":
        "Ticket assigned"
    }


@router.get("/agents/{agent_id}/tickets")
def get_agent_tickets(
    agent_id: int,
    db: Session = Depends(get_db)
):

    return db.query(Complaint).filter(
        Complaint.agent_id == agent_id
    ).all()


@router.post("/tickets/{ticket_id}/resolution")
def create_resolution(
    ticket_id: int,
    resolution: ResolutionCreate,
    db: Session = Depends(get_db)
):

    ticket = db.query(Complaint).filter(
        Complaint.id == ticket_id
    ).first()

    if not ticket:

        raise HTTPException(
            status_code=404,
            detail="Ticket not found"
        )

    new_resolution = Resolution(
        ticket_id=ticket_id,
        resolution_note=resolution.resolution_note,
        resolved_by=resolution.resolved_by
    )

    db.add(new_resolution)

    ticket.status = "Resolved"

    db.commit()

    return {
        "message":
        "Resolution added"
    }


@router.get("/tickets/{ticket_id}/history")
def resolution_history(
    ticket_id: int,
    db: Session = Depends(get_db)
):

    return db.query(Resolution).filter(
        Resolution.ticket_id == ticket_id
    ).all()
