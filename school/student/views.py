from django.shortcuts import render ,redirect
from .models import student
from .form import studentForm
# Create your views here.
def home(request):
    return render(request,'student/home.html')
def studentf(request):
    return render(request,'student/student.html')
def exam(request):
    return render(request,'student/exam.html')

# CRUD OPERATION 
#CREAT DATA
def addStudent(request):
    form = studentForm()
    if request.method == 'POST' :
        form = studentForm(request.POST)
        if form.is_valid :
            form.save()
            redirect('home')
    return render(request , 'student/studentForm.html',{'form': form})




    
        



