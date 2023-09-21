from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.
class Make(models.Model):
    name = models.CharField(max_length=50,validators=[MinLengthValidator(2, "Make must be greater than 1 character")])
    def __str__(self):
        return self.name


class Auto(models.Model):
    nickname = models.CharField(max_length=100,validators=[MinLengthValidator(2, "Make must be greater than 1 character")])
    make = models.ForeignKey(Make,on_delete=models.CASCADE)
    mileage = models.FloatField(default=0)
    comments = models.TextField()
    def __str__(self):
        return self.nickname