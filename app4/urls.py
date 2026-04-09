from django.urls import path
from . import views

app_name = 'app4'

urlpatterns = [
    path('', views.index, name='index'),
]
