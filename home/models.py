from django.db import models
# Create your models here.

class Coontact(models.Model):
    name=models.CharField(max_length=150,default='')
    email=models.EmailField(max_length=150,default='')
    phone=models.CharField(max_length=12,default='')
    desc=models.TextField(max_length=300,default='')
    date=models.DateField()

    def __str__(self):
        return self.name