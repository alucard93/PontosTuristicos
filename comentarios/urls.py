from django.urls import path
from . import views

urlpatterns = [
    path("comentarios/", views.ComentariosView.as_view()),
]
