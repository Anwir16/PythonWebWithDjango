from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class History(models.Model):
    CHOICES = [
        ('H' , 'House'),
        ('P' , 'Player'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    house = models.CharField(max_length=50, blank=False, null=False)
    player = models.CharField(max_length=50, blank=False, null=False)
    result = models.CharField(max_length=6, choices=CHOICES)
    match_id = models.CharField(max_length=6, blank=False, null=False)
    reward_point = models.IntegerField()
    point =  models.IntegerField()
    
    class Meta:
        verbose_name_plural = "Round Histories"