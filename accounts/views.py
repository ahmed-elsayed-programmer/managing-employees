from django.shortcuts import render
from django.views import View
from .models import Employee
# Create your views here.


class IndexView(View):

  def get(self , request):
    employees = Employee.objects.all()
    context = {'emps' : employees}

    return render(request , 'home.html' , context )