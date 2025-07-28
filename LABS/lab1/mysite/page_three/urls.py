from django.urls import path
from . import views
urlpatterns=[
    path('',views.home,name='page_three_home'),
]