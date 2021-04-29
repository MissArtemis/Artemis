from app.db.database import Base
from sqlalchemy import Column, Integer, String


class User(Base):
    __tablename__ = "user_info"

    id = Column(Integer, primary_key=True, index=True)
    user_name = Column(String, unique=True)
    password = Column(String)
    email = Column(String)
    phone = Column(String)