from django.db import models

# Create your models here.
class Phone(models.Model):
    name=models.CharField(max_length=122)
    phone=models.CharField(max_length=10)
    email=models.CharField(max_length=122)
    desc=models.TextField()
    date=models.DateField()

    def __str__(self):
        return self.name
    

