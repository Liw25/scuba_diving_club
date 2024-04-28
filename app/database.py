from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.orm import declarative_base

# Configuration for the database URL
DATABASE_URL = "sqlite:///scuba_diving_club.db"

# Create an engine
engine = create_engine(DATABASE_URL, echo=True)

# Create a scoped session
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

# Base class for models
Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    import models  # This is to ensure all modules are loaded before creating the tables
    Base.metadata.create_all(bind=engine)


def get_db():
    """ Dependency that can be used to get a database session.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



if __name__ == "__main__":
    # Create the database tables if running this script directly
    init_db()
