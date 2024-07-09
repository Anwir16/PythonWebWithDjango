from django import forms
from django.db import models
from django.contrib.auth.models import User

import django.db
# Create your models here.
class PaymentForm(forms.Form):
    order_id = forms.CharField(max_length=250)
    amount = forms.IntegerField()
    order_desc = forms.CharField(max_length=100)
    bank_code = forms.CharField(max_length=20, required=False)
    language = forms.CharField(max_length=2)
    point = forms.IntegerField()
    combo_point = forms.IntegerField()
    
class ComboPoint(models.Model):
    name = models.CharField(max_length=60, blank=False, null=False, default='point')
    desc = models.CharField(max_length=500, blank= True, null=True, default='point')
    image = models.ImageField(default='points/default.png', upload_to='points/')
    price = models.IntegerField()
    point = models.IntegerField()
    class Meta:
        verbose_name_plural = "Combo Points"
class PaymentHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    combo_point= models.ForeignKey(ComboPoint, on_delete=models.CASCADE)  
    order_id = models.CharField(max_length=8)
    amount = models.IntegerField()
    order_desc = models.CharField(max_length=100)
    order_date = models.DateTimeField()
    
    class Meta:
        verbose_name_plural = "Payment Histories"