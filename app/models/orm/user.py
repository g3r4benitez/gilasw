import secrets
from sqlalchemy import Column, Integer, String
from app.models.orm import Base


class User(Base):
    __tablename__: str = "user"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    lastname = Column(String(255))
    email = Column(String(255), unique=True)
    apikey = Column(String(255))

    def __init__(self, name, lastname, email):
        self.name = name
        self.lastname = lastname
        self.email = email
        self.apikey = self.generate_apikey()

    def generate_apikey(self):
        return secrets.token_hex(20)

    def __str__(self):
        return {"apikey": self.apikey}


