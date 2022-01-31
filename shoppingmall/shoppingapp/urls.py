from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('admin', views.admin, name='admin'),   #redirect to admin login page admin.html
    path('emplogin', views.emplogin, name='emplogin'),  #redirect to employee login page emplogin.html
    path('loginadmin', views.loginadmin, name='loginadmin'),    #redirect to admin login function for login
    path('home', views.home, name='home'),      #after admin login goto adminhome.html
    path('logout', views.logout, name='logout'),
    path('addemp', views.addemp, name='addemp'),    #employee add form
    path('showempdetails', views.showempdetails, name='showempdetails'),
    path('empdel/<int:id>', views.empdel, name='empdel'),
    path('empedit/<int:id>', views.empedit, name='empedit'),
    path('empedit/updateemprecord', views.updateemprecord, name='updateemprecord'),
    ################employee sections###########
    path('emplogin2', views.emplogin2, name='emplogin2'), #this is employee login function, redirect to employee login function 'emplogin2'
    path('emphome2', views.emphome2, name='emphome2'), #this url help to employee for manage session
    path('logout2', views.logout2, name='logout2'), #this usl helps to employee for logout from their session
]