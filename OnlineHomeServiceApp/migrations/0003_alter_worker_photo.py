# Generated by Django 4.0.4 on 2022-06-15 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OnlineHomeServiceApp', '0002_alter_worker_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worker',
            name='photo',
            field=models.ImageField(upload_to='uploads'),
        ),
    ]
