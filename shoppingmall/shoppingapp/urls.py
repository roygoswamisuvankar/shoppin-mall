from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('admin', views.admin, name='admin'),
    path('employee', views.employee, name='employee'),
    path('loginadmin', views.loginadmin, name='loginadmin'),
    path('home', views.home, name='home'),
    path('logout', views.logout, name='logout'),
    path('addemp', views.addemp, name='addemp'),
    path('showempdetails', views.showempdetails, name='showempdetails'),
]