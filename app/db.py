from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


CONNEXION_STRING = "mysql://uche:KD7eMgYx@localhost:3310/gestion_des_contacts"

engine = create_engine(CONNEXION_STRING)

SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try: 
        yield db
    finally:
        db.close()

