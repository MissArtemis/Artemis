from pydantic import BaseModel


class UserBase(BaseModel):
    user_name: str
    password: str


class UserCreate(UserBase):
    email: str
    phone: str


class User(UserBase):
    id: int
    email: str
    phone: str

    class Config:
        orm_mode = True

