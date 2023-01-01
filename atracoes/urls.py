from django.urls import path
from . import views

urlpatterns = [
    path("atracoes/", views.AtracoesView.as_view()),

]
