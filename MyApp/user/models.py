from django.db import models
from django.contrib.auth.models import User
from datetime import date

# Create your models here.
class Profile(models.Model):
    CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='images/default.png', upload_to='images/')
    gender = models.CharField(max_length=6, choices=CHOICES, default='Other')
    birthday = models.DateField(default=date(2000, 1, 1))
    point = models.IntegerField(default=60)

    def __str__(self):
        return f'{self.user.username} Profile'