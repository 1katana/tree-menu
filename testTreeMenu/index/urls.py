
from django.urls import path
from . import views

urlpatterns=[
    path('', views.index),
    path('d1', views.d1),
    path('d2', views.d2),
    path('d3', views.d3),
    path('d4', views.d4),
    path('d5', views.d5),
    path('d6', views.d6),
    path('d7', views.d7),
    path('d8', views.d8),
    path('d9', views.d9),
]