from sqlalchemy.exc import IntegrityError
from fastapi import status
from fastapi_sqlalchemy import db

from app.models import user as models
from app.models.orm import user as orm
from app.exceptions.general_exeptions import ConflictExeption


def get(_id: int):
    return db.session.query(orm.User).filter(orm.User.id == _id).first()


def create(user: models.User):
    try:
        entity = orm.User(**user.dict())
        db.session.add(entity)
        db.session.commit()
        return entity
    except IntegrityError as error:
        raise ConflictExeption("Email in use")


def get(email: str):
    return db.session.query(orm.User).filter(orm.User.email == email).first()


def get_user_using_apikey(apikey: str):
    return db.session.query(orm.User).filter(orm.User.apikey == apikey).first()
