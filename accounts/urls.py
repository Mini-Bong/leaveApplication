from django.urls import path
from . import views

urlpatterns = [
    path('', views.nav, name='nav'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('HOD/', views.HOD, name='HOD'),
    path('logout/', views.logout, name='logout'),
    path('logout_hod/', views.logout_hod, name='logout_hod'),
    path('resetpsw/', views.resetpsw, name='resetpsw'),
]
