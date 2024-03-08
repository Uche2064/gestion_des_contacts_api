from sqlalchemy import Column, String, TIMESTAMP, Integer, Boolean, Date
from sqlalchemy.sql.expression import text
from .db import Base

class Contact(Base):
    __tablename__ = "contact"
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    nom = Column(String(100),  nullable=False)
    prenom = Column(String(100))
    telephone = Column(String(20), index=True, unique=True)
    email = Column(String(150), index=True, unique=True)
    adresse = Column(String(200))
    profession = Column(String(200))
    date_anniv = Column(Date)
    date_ajout = Column(TIMESTAMP(timezone=True), server_default=text("now()"))
    date_modif = Column(TIMESTAMP(timezone=True), server_default=text("now()"))
    est_supprimer = Column(Boolean, server_default=text("false"))