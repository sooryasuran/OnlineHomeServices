# Generated by Django 4.0.4 on 2022-07-14 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OnlineHomeServiceApp', '0011_alter_creditcard_card_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creditcard',
            name='card_cvv',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
