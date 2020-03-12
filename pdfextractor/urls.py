from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='pdfexe-home'),
    path('about/', views.about, name='pdfexe-about'),
]
