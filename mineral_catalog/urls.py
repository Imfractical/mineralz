"""mineral_catalog URL configuration"""
from django.views.generic import RedirectView
from django.urls import path, re_path

from . import views

app_name = 'catalog'
urlpatterns = [
    path('', views.redirect_home),
    path('list/', views.list_minerals, name='list'),
    re_path(r'^list/(?P<filter>[a-zA-Z])/$', views.list_minerals, name='list_by'),
    path('view/<slug:mineral_slug>/', views.detail_mineral, name='detail'),
    path('view/', RedirectView.as_view(pattern_name='catalog:list'))
]
