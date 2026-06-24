from fastapi import APIRouter

from database import SessionLocal

from models.complaint import Complaint

from services.sla_service import check_sla

router = APIRouter(
    prefix="/reports",
    tags=["Reports"]
)


@router.get("/overdue-tickets")
def overdue_tickets():

    db = SessionLocal()

    tickets = db.query(Complaint).all()

    overdue = []

    for ticket in tickets:

        if not check_sla(
            ticket.priority,
            ticket.created_at
        ):

            overdue.append({
                "ticket_id": ticket.id,
                "title": ticket.title,
                "priority": ticket.priority,
                "status": ticket.status
            })

    return overdue


@router.get("/sla-compliance")
def sla_compliance():

    db = SessionLocal()

    tickets = db.query(Complaint).all()

    total = len(tickets)

    compliant = 0

    for ticket in tickets:

        if check_sla(
            ticket.priority,
            ticket.created_at
        ):

            compliant += 1

    percentage = 0

    if total > 0:

        percentage = (
            compliant / total
        ) * 100

    return {
        "total_tickets": total,
        "sla_compliant": compliant,
        "sla_percentage": round(
            percentage,
            2
        )
    }
