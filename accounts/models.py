from django.db import models


class Employee(models.Model):
  name = models.CharField(max_length=120)
  address = models.CharField(max_length=120)
  job_title = models.CharField(max_length=120)
  age = models.DateField() 
  email = models.EmailField(max_length=120 ,unique=True)
  phone = models.CharField(max_length=25 , unique=True)

  def __str__(self):
    return self.name 