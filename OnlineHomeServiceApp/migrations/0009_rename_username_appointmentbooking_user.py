# Generated by Django 4.0.4 on 2022-07-07 07:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('OnlineHomeServiceApp', '0008_alter_appointmentbooking_username'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointmentbooking',
            old_name='username',
            new_name='user',
        ),
    ]