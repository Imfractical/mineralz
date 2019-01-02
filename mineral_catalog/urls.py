"""mineral_catalog URL configuration"""
from django.views.generic.base import RedirectView
from django.urls import path, re_path

from . import views

app_name = 'catalog'
urlpatterns = [
    path('', views.redirect_to_list),
    re_path(r'^list\/(?P<letter>[a-zA-Z])$', views.list_minerals_by_letter, name='list'),
    path('list/group/<group>', views.list_minerals_by_group, name='list_by_group'),
    path('list/group/', RedirectView.as_view(pattern_name='catalog:list', permanent=True)),
    path('list/', views.redirect_to_list),
    path('view/<slug:mineral_slug>/', views.detail_mineral, name='detail'),
    path('view/', views.redirect_to_list),
    path('search/', views.search, name='search'),
    path('search/color/', views.search_by_color, name='search_by_color'),
]
