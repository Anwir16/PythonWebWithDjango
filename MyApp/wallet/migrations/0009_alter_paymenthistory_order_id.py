# Generated by Django 5.0.6 on 2024-08-02 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0008_alter_combopoint_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymenthistory',
            name='order_id',
            field=models.CharField(max_length=250),
        ),
    ]