# Generated by Django 4.0.4 on 2022-06-15 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OnlineHomeServiceApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worker',
            name='photo',
            field=models.ImageField(upload_to='uploads/'),
        ),
    ]
