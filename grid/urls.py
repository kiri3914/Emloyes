from django.urls import path
from .views import index, get_employee


urlpatterns = [
    path('', index, name='index'),
    path('employee/<str:slug>', get_employee, name='employee')
]

