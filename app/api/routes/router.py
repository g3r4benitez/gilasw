from fastapi import APIRouter

from app.controllers import ping_controller as ping
from app.controllers import user_controller as user
from app.controllers import category_controller as category
from app.controllers import notification_controller as notification
from app.controllers import site_controller as site
from app.core.config import API_PREFIX

api_router = APIRouter(prefix=API_PREFIX)
api_router.include_router(ping.router, tags=["ping"], prefix="/ping")
api_router.include_router(user.router, tags=["user"], prefix="/api/user")
api_router.include_router(category.router, tags=["category"], prefix="/api/category")
api_router.include_router(notification.router, tags=["notification"], prefix="/api/notification")
api_router.include_router(site.router, tags=["site"], prefix="")


