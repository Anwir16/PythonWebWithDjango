# Generated by Django 5.0.6 on 2024-06-28 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='user/img/default.png', upload_to='profile'),
        ),
    ]
