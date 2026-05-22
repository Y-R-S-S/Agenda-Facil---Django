from django.urls import path
from . import views

urlpatterns = [
    path('', views.senha, name='senha'),
    path('cadastro/', views.cadastro, name='cadastro'),
]