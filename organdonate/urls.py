from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('donor', views.donor, name ='donor'),
    path('receiver', views.receiver, name = 'receiver'),
    path('ad', views.ad, name = 'admin'),
    path('eyedonor', views.eyedonor, name = 'eyedonor'),
    path('lungsdonor', views.lungsdonor, name = 'lungsdonor'),
    path('heartdonor', views.heartdonor, name = 'heartdonor'),
    path('kidneydonor', views.kidneydonor, name = 'kidneydonor'),
   
    path('eye',views.eye,name='eye'),
    path('eye2',views.eye2,name='eye2'),
    path('register',views.register,name='register'),
    path('registration',views.registration,name='registration'),
    path('heart',views.heart,name="heart"),
    path('heart2',views.heart2,name="heart2"),
    path('lungs',views.lungs,name="lungs"),
    path('lungs2',views.lungs2,name="lungs2"),
    path('kidney',views.kidney,name="kidney"),
    path('kidney2',views.kidney2,name="kidney2"),
    path('delete/<str:pk>',views.delete,name='delete'),
    path('more_info',views.more_info,name='more_info'),
    path('more_info2',views.more_info2,name='more_info2'),
    path('about_us',views.about_us,name='about_us'),
]