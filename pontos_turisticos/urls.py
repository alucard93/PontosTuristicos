from django.urls import path
from . import views

urlpatterns = [
    path("pontos_turisticos/", views.PontoTuristicoView.as_view()),

]
