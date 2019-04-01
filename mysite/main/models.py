from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserResponse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    response1 = models.CharField(max_length = 10)
    response2 = models.CharField(max_length = 10)
    response3 = models.CharField(max_length = 10)
    response4 = models.CharField(max_length = 10)
    response5 = models.CharField(max_length = 10)
