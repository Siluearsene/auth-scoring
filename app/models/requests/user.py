from datetime import date, datetime
from uuid import UUID
from pydantic import BaseModel, EmailStr, Field


class User(BaseModel):
    name : str = Field(..., min_length=2, max_length=50)
    matricule : str = Field(..., min_length=2, max_length=50)
    email: EmailStr
    password :  str = Field(..., min_length=4, max_length=50)

class UserResponse(BaseModel):
    id: UUID
    name: str
    matricule : str 
    email: str

class UserBase(BaseModel):
    matricule: str
    name: str
    email: EmailStr


class UserCreate(UserBase):
    matricule: str | None = None
    password: str


class UserUpdate(UserBase):
    password: str | None


class UserInDB(UserBase):
    id: UUID

    class ConfigDict:
        from_attributes = True
    