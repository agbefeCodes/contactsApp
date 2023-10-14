from fastapi import Response, status, HTTPException, Depends, APIRouter
from typing import List
from sqlalchemy.orm import Session
from ..schemas import StatesResponse
from ..db import get_db
router= APIRouter()

@router.get("/states/{country_id}", response_model=list[StatesResponse])
def get_states(country_id: int, db: Session = Depends(get_db)):
    states = db.query(State).filter(State.Country_id == country_id).all()
    return states
