from fastapi import APIRouter
from starlette import status

from app.repositories import user_repository
from app.core.celery_worker import send_notification_task


router = APIRouter()


@router.post(
    "",
    status_code=status.HTTP_201_CREATED,
    dependencies=[]
)
async def post_create(category_id: int, message: str):
    # validate category and message

    # send message to all users
    users = user_repository.get_users_by_category(category_id)
    for user in users:
        channels = user.channels.split(",")
        for channel in channels:
            send_notification_task.delay(message, channel, user.id)
    return None

