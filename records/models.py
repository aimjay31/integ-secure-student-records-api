from django.db import models
from django.contrib.auth.models import User

class StudentRecord(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    year_level = models.IntegerField()
