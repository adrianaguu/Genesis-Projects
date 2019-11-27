from django.urls import path
from . import views

"""Registro de las urls de la aplicación"""
urlpatterns = [
    path('', views.type_event_list, name='type_event_list'),
    path('eventos/<int:pk>/', views.event_list, name='event_list'),
    path('evento/<int:pk>/', views.event, name='event'),
    path('inscripcion/<int:pk>/', views.inscripcion, name='inscripcion'),
    path('control_materiales/<int:pk>/', views.control_materiales, name='control_materiales'),
    path('control_asistencia/<int:pk>/', views.control_asistencia, name='control_asistencia'),
]