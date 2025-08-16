from django.shortcuts import render
from .models import Teacher
# Create your views here.
def base(request):
    return render(request,'base.html')
def home(request):
    return render(request,'home.html')
def touch(request):
    teachers = Teacher.objects.all()
    return render(request,'touch.html',{'teachers': teachers})
def stud(request):
    return render(request,'stud.html')
def deletstud(request):
    return render(request,'deletsdud.html')

