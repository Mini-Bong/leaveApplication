from django.urls import path
from . import views

urlpatterns = [
    path('', views.userhome, name='home'), 
    path('hod_CSE/', views.hod_CSE, name='hod_CSE'),
    path('hod_EEE/', views.hod_EEE, name='hod_EEE'),
    path('hod_ECE/', views.hod_ECE, name='hod_ECE'),
    path('hod_EIE/', views.hod_EIE, name='hod_EIE'),
    path('hod_Civil/', views.hod_Civil, name='hod_Civil'),
    path('hod_Mech/', views.hod_Mech, name='hod_Mech'),
    path('show_app/', views.show_app, name = 'show_app'),
    path('app/', views.app, name = 'app'),

 ]
