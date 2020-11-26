from django.urls import path
from . import views

urlpatterns = [
    path('eventos/<int:pk>/', views.eventoShow, name="eventoShow"),
    path('eventos/create/', views.eventoCreate, name="eventoCreate"),
    path('eventos/<int:pk>/edit/', views.eventoUpdate, name="eventoUpdate"),
    path('eventos/<int:pk>/delete/', views.eventoDelete, name="eventoDelete"),
    path('materiales/create/', views.MaterialCreate.as_view(), name="materialCreate"),
    path('materiales/<int:pk>/edit/', views.MaterialUpdate.as_view(), name="materialUpdate"),
    path('materiales/<int:pk>/delete/', views.MaterialDelete.as_view(), name="materialDelete"),
    path('ambientes/create/', views.AmbienteCreate.as_view(), name="ambienteCreate"),
    path('ambientes/<int:pk>/edit/', views.AmbienteUpdate.as_view(), name="ambienteUpdate"),
    path('ambientes/<int:pk>/delete/', views.AmbienteDelete.as_view(), name="ambienteDelete"),
    path('ponentes/create/', views.PonenteCreate.as_view(), name="ponenteCreate"),
    path('ponentes/<int:pk>/edit/', views.PonenteUpdate.as_view(), name="ponenteUpdate"),
    path('ponentes/<int:pk>/delete/', views.PonenteDelete.as_view(), name="ponenteDelete"),
]
