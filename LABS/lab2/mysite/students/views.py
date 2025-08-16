from django.shortcuts import render

# Create your views here.
def index(request):
    name={"fname":"Abdalaziz"}
    return render(request,'index.html',name)
def home(request):
    return render(request,'home.html')
def delet_students(request):
    return render(request,'deletstudents.html')

def show_students(request):
    students={
        "name":"abdalaziz",
        "marks":[60,70,80,90],
        "echosub":{
            "software engineering":80,
            "image processing":70,
            "clint and server":90}}
    return render(request,'showstudents.html',students)

def edit_students(request):
    students={
        "titol":230,
        "marks":{
            "software engineering":80,
            "image processing":70,
            "clint and server":90}
    }
    return render(request,'editstudents.html',students)

    
