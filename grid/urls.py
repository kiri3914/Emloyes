from unicodedata import name
from django.urls import path
from .views import index, get_employee, get_visit_day, add_visit


urlpatterns = [
    path('', index, name='index'),
    path('employee/<str:slug>', get_employee, name='employee'),
    path('list-visit/', get_visit_day, name='get_visit_day'),
    path('add-visit/', add_visit, name='add_visit')
]


