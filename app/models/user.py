from pydantic import BaseModel, EmailStr


class User(BaseModel):
    name: str
    lastname: str
    email: EmailStr

    class Config:
        orm_mode = True
