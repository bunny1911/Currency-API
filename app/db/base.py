from os import environ
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session, declarative_base


# Database variables
DB_USER:     str = environ.get("DB_USER")
DB_PASSWORD: str = environ.get("DB_PASSWORD")
DB_HOST:     str = environ.get("DB_HOST")
DB_NAME:     str = environ.get("DB_NAME")
DB_ECHO:     str = environ.get("DB_ECHO")

# Connection to artur_db
URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
engine = create_engine(URL, echo=DB_ECHO)

# Create Session
Session = sessionmaker(bind=engine)
session = scoped_session(Session)

# Create database model
Base = declarative_base()
