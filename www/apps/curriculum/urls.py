from django.urls import path
from . import views


urlpatterns = [
    path('', views.curriculum, name='curriculum'),
    path('generate_pdf', views.generate_pdf, name='generate_pdf'),
]
