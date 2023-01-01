from django.urls import path
from . import views

urlpatterns = [
    path("avaliacoes/", views.AvaliacoesView.as_view()),

]
