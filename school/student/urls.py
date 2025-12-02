from django.urls import path
from . import views
from .form import studentForm
urlpatterns = [
    path('',views.home, name = 'home'),
    path('student/',views.student, name = 'student'),
    
    path('addStudent',views.addStudent,name='addStudent')
]