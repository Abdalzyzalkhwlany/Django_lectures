from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('home/',views.home,name='home'),
    path('deletstudents/',views.delet_students,name='deletstudents'),
    path('showstudents/',views.show_students,name='showstudents'),
    path('editstudents/',views.edit_students,name='editstudents'),
]