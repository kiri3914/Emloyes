from django.shortcuts import render
from .models import Employee, Visit


def index(request):
    employers = Employee.objects.all()
    context = {
        'employers': employers
    }
    return render(request, 'show.html', context)



def get_employee(request, slug):
    visit = Visit.objects.filter(employer__slug=slug)
    employee = Employee.objects.get(slug=slug)

    context = {
        'visits': visit,
        'employee': employee
    }
    return render(request, 'get_employee.html', context)
