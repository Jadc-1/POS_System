from sqlmodel import SQLModel, create_engine
from .model import Products, Categorys

sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, echo=False)

def reset_data():
    SQLModel.metadata.drop_all(engine)
    SQLModel.metadata.create_all(engine)

if __name__ == "__main__":
    SQLModel.metadata.create_all(engine)
    
    