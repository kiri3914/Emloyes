from django.db import models
from django.urls import reverse

CHOICES = (
    (True, 'Посетил(а)'),
    (False, "Отсутствовал(а)")
)


class Position(models.Model):
    title = models.CharField(max_length=244, blank=True, null=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title


class Employee(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=55)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='employers/')
    stack = models.CharField(max_length=1000, blank=True, null=True)
    slug = models.SlugField(unique=True)

    def get_absolute_url(self):
        return reverse('visit', kwargs={'slug': self.slug})

    def __str__(self):
        return self.name


class Visit(models.Model):
    date = models.DateField()
    employer = models.ForeignKey(Employee, on_delete=models.CASCADE)