from fastapi import Response, status, HTTPException, Depends, APIRouter
from typing import List
from sqlalchemy.orm import Session
from ..schemas import CountriesResponse
from ..db import get_db

router= APIRouter()

@router.get("/countries", response_model=List[CountriesResponse])
def get_countries(db: Session = Depends(get_db)):
    countries = db.query(Country).all()
    return countries