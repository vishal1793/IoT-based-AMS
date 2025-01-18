from django.urls import path
from app import views

urlpatterns=[
    path('',views.home,name='home'),
    path('reg/', views.reg, name='reg'),
    path('UID/', views.UID, name='UID'),
    path('inloc/', views.inloc, name='in_loc'),
    path('outloc/', views.outloc, name='out_loc'),
    path('save-rfid-data/', views.save_rfid_data, name='save_rfid_data')
]