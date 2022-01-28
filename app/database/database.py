from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# SQLALCHEMY_DATABASE_URL = "postgresql://postgres:postgres@localhost/Space_Flight_News_Challenge"
SQLALCHEMY_DATABASE_URL = 'postgres://oelucwrdopakiw:22cb024f07283c0d0982164786374b40bd4f0b7107d4ba3e4ff19fdb6203a0ff@ec2-54-224-64-114.compute-1.amazonaws.com:5432/d8r0usr9c6l03k'


engine = create_engine(SQLALCHEMY_DATABASE_URL)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base = declarative_base()


def get_db():
    # Creates a session query
    db = SessionLocal()
    try:
        # Wait until it's used
        yield db
    finally:
        # Close the connection
        db.close()
