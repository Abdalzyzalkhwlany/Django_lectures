from django.urls import path
from . import views
urlpatterns=[
    path('',views.base,name="base"),
    path('home/',views.home,name="home"),
    path('touch/',views.touch,name="touch"),
    path('stud/',views.stud,name="stud"),
    path('deletstud/',views.deletstud,name="deletstud"),
]