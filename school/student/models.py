from django.db import models

# Create your models here.
class student(models.Model):
    name =models.CharField(max_length=200)
    age = models.IntegerField(max_length=24)
    grade = models.CharField(max_length=2)

    def __str__(self):
        return self.name
    