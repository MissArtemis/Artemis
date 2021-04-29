from sqlalchemy.orm import Session
from app.user import models
from app.user import schemas


def get_user(db: Session, user_name: str):
    return db.query(models.User).filter(models.User.user_name == user_name).first()


def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(user_name=user.user_name, password=user.password, email=user.email, phone=user.phone)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


