from fastapi import FastAPI
from .db import engine
from . import models, contact

app = FastAPI()

try:    
    models.Base.metadata.create_all(bind=engine)
    print("connexion réussie")
except Exception as e:
    print(e)
    
app.include_router(contact.router)