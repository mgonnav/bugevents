from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),

    path('dashboard/', views.dashboard, name="dashboard"),
    path('recursos/', views.recursos, name="recursos"),
    path('recursos/ambientes/', views.ambienteIndex, name="ambienteIndex"),
    path('recursos/materiales/', views.materialIndex, name="materialIndex"),
    path('recursos/ponentes/', views.ponenteIndex, name="ponenteIndex"),

    #path('usuarios/', views.usuarios, name="usuarios"),

    path('reset_password/', auth_views.PasswordResetView.as_view(), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
]
