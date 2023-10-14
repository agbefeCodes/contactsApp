from fastapi import Response, status, HTTPException, Depends, APIRouter
from typing import List
from sqlalchemy.orm import Session
from ..utils import get_info
from ..schemas import ContactPost, ContactPostResponse
from ..db import get_db
from ..models import Contacts

router = APIRouter()


@router.post("/contacts", response_model=ContactPostResponse)
def add_contact(contact: ContactPost, db: Session = Depends(get_db)):
    contact_info = contact.dict()
    stateid = contact_info["StateId"]
    email = contact_info["Email"]

    new_contact = Contacts(**contact.dict())

    db.add(new_contact)
    db.commit()
    db.refresh(new_contact)

    contact_id = (
        db.query(Contacts).filter(Contacts.Email == contact_info["Email"]).first()
    )
    contact_info = get_info(email=email, stateid=stateid, db=db)
    return contact_info


@router.put("/contacts/{contact_id}")
def update_contact(
    new_info: ContactPost, contact_id: int, db: Session = Depends(get_db)
):
    stateid = new_info.dict()["StateId"]
    email = new_info.dict().get("Email")
    contact = db.query(Contacts).filter(Contacts.id == contact_id)
    email_query = db.query(Contacts).filter(Contacts.Email == email)
    if email_query:
        raise HTTPException(
            status_code=status.HTTP_226_IM_USED, detail=f"Email already exist"
        )

    if not contact.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"contact with id: {contact_id} not found",
        )
    contact.update(new_info.dict(), synchronize_session=False)
    db.commit()
    contact_info = get_info(db=db, stateid=stateid, email=email)
    return contact_info


@router.get("/contacts/{contact_id}", response_model=ContactPostResponse)
def get_contact(contact_id: int, db: Session = Depends(get_db)):
    contact = db.query(Contacts).filter(Contacts.id == contact_id).first()
    if not contact:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"contact with id: {contact_id} not found",
        )
    contact_info = get_info(email=contact.Email, stateid=contact.StateId, db=db)
    return contact_info


@router.delete("/contacts/{contact_id}", status_code=status.HTTP_404_NOT_FOUND)
def delet_contact(contact_id: int, db: Session = Depends(get_db)):
    contact = db.query(Contacts).filter(Contacts.id == contact_id)

    if not contact.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"contact with id: {contact_id} not found",
        )

    contact.delete(synchronize_session=False)
    # db.delete(contact.first())
    db.commit()
