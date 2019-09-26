from main_app import views
from . import views #el punto nos manda a raiz
from django.urls import path

urlpatterns = [
    path('',views.index),
]