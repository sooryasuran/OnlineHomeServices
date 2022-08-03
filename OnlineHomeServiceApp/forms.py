import re

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

from OnlineHomeServiceApp.models import Login, Worker, Customer, AppointmentSchedule, AppointmentBooking, Bill, \
    CreditCard, Feedback


def phone_number_validator(value):
    if not re.compile(r'^[7-9]\d{9}$').match(value):
        raise ValidationError('This is Not a Valid Phone Number')

class DateInput(forms.DateInput):
    input_type = 'date'

class LoginForm(UserCreationForm):
    username = forms.CharField()
    password1 = forms.CharField(label='Password',widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password',widget=forms.PasswordInput)
    class Meta:
        model = Login
        fields = ('username','password1','password2')

CATEGORY = (('Dry-Cleaning Pickup & Delivery','Dry-Cleaning Pickup & Delivery'),
            ('Repairing fences, doors, windows','Repairing fences, doors, windows'),('Plumbing and electrical repairs','Plumbing and electrical repairs'),('Personal Chef','Personal Chef'),('Mobile Car-Wash and Detailing','Mobile Car-Wash and Detailing'),('Home nursing','Home nursing'),('Pet Care','Pet Care'),('Tutoring','Tutoring'))
class WorkerForm(forms.ModelForm):
    category=forms.ChoiceField(choices=CATEGORY)
    contact_no = forms.CharField(validators=[phone_number_validator])
    class Meta:
        model = Worker
        fields=('name','area','category','contact_no','photo')

class CustomerForm(forms.ModelForm):
    contact_no = forms.CharField(validators=[phone_number_validator])
    class Meta:
        model = Customer
        fields=('name','email','contact_no','home_address','pincode')

class AppointmentScheduleForm(forms.ModelForm):
    class Meta:
        model = AppointmentSchedule
        fields = ('date','start_time','end_time')

class AppointmentBookingForm(forms.ModelForm):
    class Meta:
        models = AppointmentBooking
        fields = '__all__'

class Billaddform(forms.ModelForm):
    class Meta:
        model = Bill
        exclude = ('status','paid_date')

class Billpayform(forms.ModelForm):
    card_no = forms.CharField(validators=[RegexValidator(regex='^,{16}$',message='Please enter a valid Card No.')])
    card_cvv = forms.CharField(widget=forms.PasswordInput, validators=[RegexValidator(regex='^,{3}$',message='Please enter a valid CVV')])
    expiry_date = forms.DateField(widget=DateInput(attrs={'id':'example-month-input'}))
    class Meta:
        model = CreditCard
        fields = ('card_no','card_cvv','expiry_date')

CATEGORYNEW = (('Compaint','Complaint'),('Service Query','Service Query'))
class FeedbackForm(forms.ModelForm):
    category = forms.ChoiceField(choices=CATEGORYNEW)
    class Meta:
        model = Feedback
        fields = ('customer','date','category','comments')