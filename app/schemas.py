from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

class Contact(BaseModel):
    prenom: Optional[str] = None
    telephone: Optional[str] = None
    email: Optional[EmailStr] = None
    adresse: Optional[str] = None
    profession: Optional[str] = None
    date_anniv: Optional[datetime] = None
    date_ajout: Optional[datetime] = None
    date_modif: Optional[datetime] = None

class AddContact(Contact):
    nom: str


class ContactReponse(BaseModel):
    id: int
    nom: Optional[str] = None
    prenom: Optional[str] = None
    telephone: Optional[str] = None
    email: Optional[EmailStr] = None
    adresse: Optional[str] = None
    profession: Optional[str] = None
    date_anniv: Optional[datetime] = None
    date_ajout: Optional[datetime] = None
    date_modif: Optional[datetime] = None

class ContactUpdate(Contact):
    nom: Optional[str] = None
