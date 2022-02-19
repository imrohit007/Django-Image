from django.urls import path
from . import views

urlpatterns = [
    path('', views.ImageView, name='upload'),
    path('img/', views.Display, name='display')
]