from django.urls import path

from . import views

app_name = 'catalog'
urlpatterns = [
    path('', views.list_minerals, name='list'),
]
