from django.urls import path
from . import views

urlpatterns = [
    path("enderecos/", views.EnderecosView.as_view()),

]
