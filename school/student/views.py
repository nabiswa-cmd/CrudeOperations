from django.shortcuts import render , redirect , get_object_or_404
from .models import student
# Create your views here.
# create data 
def add(request):
    if request.method == "POST" :
        name = request.POST.get('name')
        age = request.POST.get('age')
        grade = request.POST.get('grade')

        student.objects.create(name = name , age = age , grade = grade )

        redirect('listviews')
    return render(request,'add.html')

# Read the data  from the tables
def list(request):
    Student = student.objects.all()
    return render(request ,'list.html', {'Student':Student})

