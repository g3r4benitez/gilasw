from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from starlette import status
from fastapi.templating import Jinja2Templates

from app.repositories import category_repository
from app.repositories import notification_repository

router = APIRouter()

templates = Jinja2Templates(directory="static/templates")



@router.get(
    "/index",
    status_code=status.HTTP_200_OK,
    response_class=HTMLResponse
)
def index(request: Request):

    return templates.TemplateResponse("documentation.html",
                                      {
                                          "request": request,
                                          "title": "GilaSW - Code Challenge - Gerardo Benitez",
                                          "encabezado": "Code Challenge - Gerardo Benitez",
                                        "subtitle": "Notification System",
                                          "container": "El contenido por defecto"
                                      })

@router.get(
    "/categories",
    status_code=status.HTTP_200_OK,
    response_class=HTMLResponse
)
def categories(request: Request):

    return templates.TemplateResponse("categories.html",
                                      {
                                          "request": request,
                                          "title": "GilaSW - Code Challenge - Gerardo Benitez",
                                          "encabezado": "Code Challenge - Gerardo Benitez",
                                        "subtitle": "Category List",
                                          "categories": category_repository.getall()
                                      })

@router.get(
    "/notifications",
    status_code=status.HTTP_200_OK,
    response_class=HTMLResponse
)
def notifications(request: Request):

    return templates.TemplateResponse("notifications.html",
                                      {
                                          "request": request,
                                          "title": "GilaSW - Code Challenge - Gerardo Benitez",
                                          "encabezado": "Code Challenge - Gerardo Benitez",
                                        "subtitle": "Send a Nofication",
                                          "categories": category_repository.getall()
                                      })


@router.get(
    "/messages",
    status_code=status.HTTP_200_OK,
    response_class=HTMLResponse
)
def messages(request: Request):

    return templates.TemplateResponse("messages.html",
                                      {
                                          "request": request,
                                          "title": "GilaSW - Code Challenge - Gerardo Benitez",
                                          "encabezado": "Code Challenge - Gerardo Benitez",
                                        "subtitle": "Messages",
                                          "notifications": notification_repository.getall()
                                      })
