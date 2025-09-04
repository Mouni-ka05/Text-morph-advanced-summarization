from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from dotenv import load_dotenv

load_dotenv()

MYSQL_USER = os.getenv("MYSQL_USER", "root1")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD", "root123!")
MYSQL_DB = os.getenv("MYSQL_DB", "auth_demo")
MYSQL_HOST = os.getenv("MYSQL_HOST", "localhost")

DATABASE_URL = f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}/{MYSQL_DB}"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base = declarative_base()
