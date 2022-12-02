from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('hook/', views.hook, name='hook'),
    path('add/', views.send_posts, name='add_job'),
    path('setwebhook/', views.setwebhook, name="setwebhook"),
]
