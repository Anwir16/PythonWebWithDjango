# Generated by Django 5.0.6 on 2024-07-02 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_alter_profile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='point',
            field=models.IntegerField(default=60),
        ),
    ]
