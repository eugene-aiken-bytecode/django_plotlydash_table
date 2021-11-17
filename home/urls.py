from django.urls import path
from django.conf.urls import url
from . import views
from home.dash_apps.finished_apps import simpleexample

urlpatterns = [
    path('', views.home, name='home'),
    path('get', views.get, name='get'),
    path('post', views.post, name='post'),
    path('table', views.table, name='table')
]