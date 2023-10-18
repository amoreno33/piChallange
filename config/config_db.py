from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os


DB_NAME = "../database.sqlite"
DB_DIR = os.path.dirname(os.path.realpath(__file__))
DATABASE_URL = f'sqlite:///{os.path.join(DB_DIR, DB_NAME)}'


engine = create_engine(DATABASE_URL, echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

