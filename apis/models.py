from django.db import models
from django.contrib.auth.models import AbstractUser



class CustomUser(AbstractUser):
    pass





class Vakansi(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    price = models.IntegerField()
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE) 

    def __str__(self):
        return self.title


class Worker(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  
    phone_number = models.CharField(max_length=15, unique=True)
    date_joined = models.DateField(auto_now_add=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    company = models.CharField(max_length=50, null=True)
    desc = models.TextField(null=True)

    def __str__(self):
        return f"{self.name}"
