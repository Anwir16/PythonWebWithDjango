from django import forms
from django.db import models
from django.contrib.auth.models import User

import django.db
# Create your models here.
class PaymentForm(forms.Form):
    order_id = forms.CharField(max_length=250)
    order_date = models.DateTimeField()
    amount = forms.IntegerField()
    order_desc = forms.CharField(max_length=100)
    bank_code = forms.CharField(max_length=20, required=False)
    language = forms.CharField(max_length=2)
    
class PaymentHistory(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    order_id = models.CharField(max_length=8)
    order_type = models.CharField(max_length=20)
    amount = models.IntegerField()
    order_desc = models.CharField(max_length=100)
    order_date = models.DateTimeField()
    
    class Meta:
        verbose_name_plural = "Payment Histories"