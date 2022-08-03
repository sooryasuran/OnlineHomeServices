from django.contrib import admin

# Register your models here.
from OnlineHomeServiceApp import models

admin.site.register(models.Login)
admin.site.register(models.Worker)
admin.site.register(models.Customer)
