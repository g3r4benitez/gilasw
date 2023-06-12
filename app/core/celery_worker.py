import importlib
from celery.utils.log import get_task_logger

from .celery_app import celery_app

celery_log = get_task_logger(__name__)



@celery_app.task(
    name='app.core.celery_worker.send_notification',
    )
def send_notification_task(message, channel_name, id_user):
    service = importlib.import_module(f"app.services.{channel_name}_service")
    channel = service.get_channel()
    channel.send_notification(message, id_user)
    celery_log.info(f"Sending message: {message}, using channel: {channel_name}, to user: ")


