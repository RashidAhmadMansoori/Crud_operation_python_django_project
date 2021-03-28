from django.db import models

# Create your models here.
class student(models.Model):
    id=models.CharField(max_length=20, primary_key=True)
    fullname=models.CharField(max_length=60)
    Class=models.CharField(max_length=30)
    address=models.CharField(max_length=30)
    def __str__(self):
        return self.fullname