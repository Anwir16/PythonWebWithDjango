from django.db import models

# Create your models here.
class UserRegistration(models.Model):
    user_name = models.CharField(primary_key=True, max_length=50)
    email = models.CharField(max_length=500)
    password = models.CharField(max_length=255, null=False)
    full_name = models.CharField(max_length=200)

    class Meta:
        db_table = 'FinalGame'