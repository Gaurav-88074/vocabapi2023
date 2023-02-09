import imp
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.getRoutes, name='home'),
    path('allvocab',views.getWord,  name='entire vocab collection'),
    path('addvocab',views.addVocab, name='vocab insertion'),
]
