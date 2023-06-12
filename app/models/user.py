from pydantic import BaseModel, EmailStr


class User(BaseModel):
    name: str
    email: EmailStr
    phone_number: int
    subscribed: str
    channels: str

    class Config:
        orm_mode = True
