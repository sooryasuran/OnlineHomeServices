# Generated by Django 4.0.4 on 2022-06-15 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OnlineHomeServiceApp', '0003_alter_worker_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worker',
            name='category',
            field=models.CharField(max_length=100),
        ),
    ]