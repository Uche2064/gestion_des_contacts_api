from datetime import datetime
from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy import or_
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from . import db, models, schemas
from typing import List

router = APIRouter(
    prefix="/contact",
    tags=["Contact"]
)

@router.get("/", response_model=List[schemas.ContactReponse])
async def get_contacts(db: Session = Depends(db.get_db)):
    return db.query(models.Contact).all()

@router.get("/{name}", status_code=status.HTTP_200_OK, response_model=List[schemas.ContactReponse])
async def get_specific_contact(name: str, db: Session = Depends(db.get_db)):
    get_contact = db.query(models.Contact).filter(models.Contact.nom.like(f"%{name}%")).all()
    if get_contact is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Aucun contact n'a ce nom")
    return get_contact
    
@router.post("/", status_code=status.HTTP_202_ACCEPTED ,response_model=schemas.ContactReponse)
async def add_contact(contact: schemas.AddContact, db: Session = Depends(db.get_db)):
    if contact.telephone is None:
        get_contact = db.query(models.Contact).filter(or_(models.Contact.email == contact.email)).first()
    elif contact.email is None:
        get_contact = db.query(models.Contact).filter(or_(models.Contact.email == contact.email)).first()

    if get_contact:
        raise HTTPException(status_code=status.HTTP_306_RESERVED, detail="Ce contact existe déjà")
    new_contact = models.Contact(**contact.model_dump())
    
    db.add(new_contact)
    db.commit()
    db.refresh(new_contact)
    return new_contact

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_contact(id: int,db: Session = Depends(db.get_db)):
    get_contact = db.query(models.Contact).filter(models.Contact.id == id)
    if get_contact.first() is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Contact non trouvé")
    get_contact.delete(synchronize_session=False)
    db.commit()
    
@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED, response_model=schemas.ContactReponse)
async def update_contact(id: int, contact: schemas.ContactUpdate, db: Session = Depends(db.get_db)):
    get_contact = db.query(models.Contact).filter(models.Contact.id == id)
    if get_contact.first() is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Contact non trouvé")
    try:
        if contact.email is not None and contact.telephone is not None:
            if get_contact.first().email != contact.email or get_contact.first().telephone != contact.telephone:
                existing_contact = db.query(models.Contact).filter(or_(models.Contact.email == contact.email, models.Contact.telephone == contact.telephone)).first()
                if existing_contact: 
                    raise HTTPException(status_code=status.HTTP_306_RESERVED, detail="E-mail ou numéro déjà pris")
        contact.date_modif = datetime.utcnow()
        updated_contact = contact.model_dump(exclude_unset=True)
        for key, value in updated_contact.items():
            setattr(get_contact.first(), key, value)
        db.commit()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"{e}")
    
    return get_contact.first()
