from sqlalchemy.orm import Session
from .models import Country, State, Contacts

def get_info(email: str, stateid: int, db: Session) -> dict:
    contact = db.query(Contacts).filter(Contacts.Email == email).first()
    state = db.query(State).filter(State.id == stateid).first()
    country = db.query(Country).filter(Country.id == state.Country_id).first()
    return {
        "id": contact.id,
        "Firstname": contact.Firstname,
        "Lastname": contact.Lastname,
        "Email": contact.Email,
        "MobileNo": contact.MobileNo,
        "StateId": state.id,
        "State": state.Name,
        "CountryId": country.id,
        "Country": country.Name,
    }