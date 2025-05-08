from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('table/',views.table,name="tabel"),
    path('filter1/',views.filter1,name="filter1"),


]
