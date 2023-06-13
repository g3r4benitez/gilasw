from fastapi_sqlalchemy import db

from app.models import notification as models
from app.models.orm import notification as orm


def create(notification: models.Notification):
    entity = orm.Notification(**notification.dict())
    db.session.add(entity)
    db.session.commit()
    return entity


