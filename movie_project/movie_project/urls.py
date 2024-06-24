# movie_project/urls.py

from django.contrib import admin
from django.urls import path
from films import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.film_list, name='film_list'),
    path('add/', views.add_film, name='add_film'),
]