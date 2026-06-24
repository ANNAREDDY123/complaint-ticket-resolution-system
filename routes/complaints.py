from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)

from sqlalchemy.orm import Session

from database import SessionLocal

from models.complaint import Complaint

from schemas.complaint import ComplaintCreate

router = APIRouter(
    prefix="/complaints",
    tags=["Complaints"]
)


def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


VALID_PRIORITIES = [
    "Low",
    "Medium",
    "High",
    "Critical"
]


@router.post("/")
def create_complaint(
    complaint: ComplaintCreate,
    db: Session = Depends(get_db)
):

    if not complaint.title.strip():

        raise HTTPException(
            status_code=400,
            detail="Title cannot be empty"
        )

    if complaint.priority not in VALID_PRIORITIES:

        raise HTTPException(
            status_code=400,
            detail="Invalid priority"
        )

    new_complaint = Complaint(
        title=complaint.title,
        description=complaint.description,
        category=complaint.category,
        priority=complaint.priority,
        status=complaint.status
    )

    db.add(new_complaint)

    db.commit()

    db.refresh(new_complaint)

    return new_complaint


@router.get("/")
def get_complaints(
    status: str = None,
    priority: str = None,
    page: int = 1,
    limit: int = 10,
    db: Session = Depends(get_db)
):

    query = db.query(Complaint)

    if status:
        query = query.filter(
            Complaint.status == status
        )

    if priority:
        query = query.filter(
            Complaint.priority == priority
        )

    total = query.count()

    complaints = query.offset(
        (page - 1) * limit
    ).limit(limit).all()

    return {
        "total_records": total,
        "page": page,
        "limit": limit,
        "data": complaints
    }


@router.get("/{complaint_id}")
def get_complaint(
    complaint_id: int,
    db: Session = Depends(get_db)
):

    complaint = db.query(Complaint).filter(
        Complaint.id == complaint_id
    ).first()

    if not complaint:

        raise HTTPException(
            status_code=404,
            detail="Complaint not found"
        )

    return complaint


@router.put("/{complaint_id}")
def update_complaint(
    complaint_id: int,
    complaint: ComplaintCreate,
    db: Session = Depends(get_db)
):

    db_complaint = db.query(Complaint).filter(
        Complaint.id == complaint_id
    ).first()

    if not db_complaint:

        raise HTTPException(
            status_code=404,
            detail="Complaint not found"
        )

    db_complaint.title = complaint.title
    db_complaint.description = complaint.description
    db_complaint.category = complaint.category
    db_complaint.priority = complaint.priority
    db_complaint.status = complaint.status

    db.commit()

    return {
        "message":
        "Complaint updated"
    }


@router.delete("/{complaint_id}")
def delete_complaint(
    complaint_id: int,
    db: Session = Depends(get_db)
):

    complaint = db.query(Complaint).filter(
        Complaint.id == complaint_id
    ).first()

    if not complaint:

        raise HTTPException(
            status_code=404,
            detail="Complaint not found"
        )

    db.delete(complaint)

    db.commit()

    return {
        "message":
        "Complaint deleted"
    }
