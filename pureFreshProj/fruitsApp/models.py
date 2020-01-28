from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Create your models here.
def get_admin_user():
    return User.objects.get(username='admin')

class Fruit(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET(get_admin_user))
    name = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.CharField(max_length=100)
    photo = models.FileField(upload_to='fruitsApp/images/uploaded_photos')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


