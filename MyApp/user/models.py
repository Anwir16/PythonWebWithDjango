from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to='profile')
    gender = models.CharField(max_length=6, choices=[
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ], default='Other')
    birthday = models.DateField()

    def __str__(self):
        return f'{self.user.username} Profile'