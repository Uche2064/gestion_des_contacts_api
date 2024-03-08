from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
from typing import Optional

class BaseContact(BaseModel):
    prenom: Optional[str] = None
    telephone: Optional[str] = None
    email: Optional[EmailStr] = None
    adresse: Optional[str] = None
    profession: Optional[str] = None
    date_anniv: Optional[datetime] = None
    date_ajout: Optional[datetime] = None
    date_modif: Optional[datetime] = None

class AddContact(BaseContact):
    nom: str

class ContactResponse(BaseModel):
    id: int
    nom: Optional[str] = Field(None, alias='nom')
    prenom: Optional[str] = Field(None, alias='prenom')
    email: Optional[EmailStr] = Field(None, alias='email')
    adresse: Optional[str] = Field(None, alias='adresse')
    profession: Optional[str] = Field(None, alias='profession')
    date_anniv: Optional[datetime] = Field(None, alias='date_anniv')
    date_ajout: Optional[datetime] = Field(None, alias='date_ajout')
    date_modif: Optional[datetime] = Field(None, alias='date_modif')

class ContactUpdate(BaseContact):
    nom: Optional[str] = None
