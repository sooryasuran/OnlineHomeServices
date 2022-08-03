
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class Login(AbstractUser):
    is_worker = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)

class Worker(models.Model):
    user =models.ForeignKey(Login,on_delete=models.CASCADE,related_name='worker')
    name = models.CharField(max_length=100)
    area = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    contact_no = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='uploads')
    def __str__(self):
        return self.name

class Customer(models.Model):
    user = models.ForeignKey(Login,on_delete=models.CASCADE,related_name='customer')
    name = models.CharField(max_length=100)
    email=models.EmailField()
    contact_no=models.CharField(max_length=50)
    home_address=models.CharField(max_length=250)
    pincode=models.IntegerField()
    def __str__(self):
        return self.name

class AppointmentSchedule(models.Model):
    worker = models.ForeignKey(Worker,on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

class AppointmentBooking(models.Model):
    user = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='appointment')
    schedule = models.ForeignKey(AppointmentSchedule,on_delete=models.CASCADE)
    status = models.IntegerField(default=0)

class Bill(models.Model):
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    billdate = models.DateField(auto_now_add=True)
    amount = models.IntegerField()
    paid_date = models.DateField(auto_now_add=True)
    status = models.IntegerField(default=0)

class CreditCard(models.Model):
    card_no = models.CharField(max_length=50, null=True, blank=True)
    card_cvv = models.CharField(max_length=30, null=True, blank=True)
    expiry_date = models.CharField(max_length=100, null=True, blank=True)

class Feedback(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE,null=True, blank=True)
    date = models.DateField()
    category = models.CharField(max_length=50)
    comments = models.CharField(max_length=2000)
    reply = models.TextField(null=True, blank=True)





