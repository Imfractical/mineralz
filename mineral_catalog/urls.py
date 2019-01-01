"""mineral_catalog URL configuration"""
from django.urls import path, re_path

from . import views

app_name = 'catalog'
urlpatterns = [
    path('', views.redirect_to_list),
    re_path(r'^list\/(?P<letter>[a-zA-Z])$', views.list_minerals, name='list'),
    path('list/', views.redirect_to_list),
    path('view/<slug:mineral_slug>/', views.detail_mineral, name='detail'),
    path('view/', views.redirect_to_list),
]
