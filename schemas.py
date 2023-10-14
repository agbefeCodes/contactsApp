from pydantic import BaseModel, EmailStr


class CountriesResponse(BaseModel):
    id: int
    Name: str

    class Config:
        from_attributes = True


class StatesResponse(BaseModel):
    id: int
    Country_id: int
    Name: str

    class Config:
        from_attributes = True


class ContactPost(BaseModel):
    Firstname: str
    Lastname: str
    Email: EmailStr
    MobileNo: str
    StateId: int


class ContactPostResponse(BaseModel):
    id: int
    Firstname: str
    Lastname: str
    Email: EmailStr
    MobileNo: str
    StateId: int
    State: str
    CountryId: int
    Country: str

    class Config:
        from_attributes = True
