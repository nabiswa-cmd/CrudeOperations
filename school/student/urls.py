from django.urls import path
from . import views

urlpatterns = [
    path ('',views.list, name= "listviews"),
    path('add/',views.add, name = "add")
]