from sqlmodel import SQLModel, Session, create_engine
from sqlmodel.pool import StaticPool

# Configure the database connection
DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool
)

# Create the database tables
SQLModel.metadata.create_all(engine)


# Dependency to get the database session
def get_session():
    with Session(engine) as session:
        yield session
