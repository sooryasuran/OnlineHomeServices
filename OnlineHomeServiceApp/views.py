import datetime

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


# Create your views here.
from django.template import RequestContext

from OnlineHomeServiceApp.forms import LoginForm, WorkerForm, CustomerForm, AppointmentScheduleForm, Billpayform, \
    Billaddform, FeedbackForm
from OnlineHomeServiceApp.models import Worker, Customer, Login, AppointmentSchedule, AppointmentBooking, Bill, \
    CreditCard, Feedback


def homeview(request):
    return render(request,'index.html')
def aboutus(request):
    return render(request,'aboutus.html')
def services(request):
    return render(request,'services.html')
def Contact(request):
    return render(request,'Contact.html')


def loginview(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pass')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            if user.is_staff:
                return redirect('workerview')
            elif user.is_worker:
                return redirect('workerhome')
            elif user.is_customer:
                return redirect('customerhome')
        else:
            messages.info(request,'invalid credentials')
    return render(request,'login.html')

@login_required(login_url='loginview')
def adminview(request):
    return render(request,'ADMIN/adminhome.html')

def addworker(request):
    login_form =LoginForm()
    worker_form = WorkerForm()
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        worker_form = WorkerForm(request.POST, request.FILES)
        if login_form.is_valid() and worker_form.is_valid():
            user = login_form.save(commit=False)
            user.is_worker = True
            user.save()
            w = worker_form.save(commit=False)
            w.user = user
            w.save()
            messages.info(request,'Worker Updates Successfully')
            return redirect('workerview')
    return render(request,'ADMIN/addworker.html',{'login_form':login_form,'worker_form':worker_form})

@login_required(login_url='loginview')
def workerview(request):
    wr = Worker.objects.all()
    return render(request,'ADMIN/workerview.html',{'wr':wr})

@login_required(login_url='loginview')
def workerhome(request):
    u = request.user
    profile = Worker.objects.filter(user_id=u)
    return render(request,'WORKER/workerhome.html',{'profile':profile})

@login_required(login_url='loginview')
def customerview(request):
    cr = Customer.objects.all()
    return render(request,'CUSTOMER/customerhome.html',{'cr':cr})

def customerregister(request):
    login_form = LoginForm()
    customer_form = CustomerForm()
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        customer_form = CustomerForm(request.POST)
        if login_form.is_valid() and customer_form.is_valid():
            user = login_form.save(commit=False)
            user.is_customer = True
            user.save()
            w = customer_form.save(commit=False)
            w.user = user
            w.save()
            messages.info(request, 'Customer registered Successfully')
            return redirect('customerview')
    return render(request, 'CUSTOMER/customerregister.html', {'login_form': login_form, 'customer_form': customer_form})

@login_required(login_url='loginview')
def customerhome(request):
    cr = Worker.objects.all()
    return render(request,'CUSTOMER/customerhome.html',{'cr':cr})

def logoutview(request):
    logout(request)
    return redirect('loginview')

def admincustomerview(request):
    csr = Customer.objects.all()
    return render(request,'ADMIN/admincustomerview.html',{'csr':csr})

def workercustomerview(request):
    wc = Customer.objects.all()
    return render(request,'WORKER/workercustomerview.html',{'wc':wc})

@login_required(login_url='loginview')
def workerslistupdate(request,id):
    wr = Worker.objects.get(id=id)
    lw = Login.objects.get(worker=wr)
    if request.method == 'POST':
        form = WorkerForm(request.POST or None, instance=wr)
        login_form = LoginForm(request.POST or None,instance=lw)
        if form.is_valid() and login_form.is_valid():
            form.save()
            login_form.save()
            messages.info(request,'Worker List Updated Successfully')
            return redirect('workerview')
    else:
        form = WorkerForm(instance=wr)
        login_form =LoginForm(instance=lw)
    return render(request,'ADMIN/workerupdate.html',{'form':form,'login_form':login_form})


def workerdelete(request, id):
    wr = Worker.objects.get(id=id)
    lg = Login.objects.get(worker=wr)
    if request.method == 'POST':
        lg.delete()
        messages.info(request,'Worker deleted successfully')
        return redirect('workerview')
    else:
        return redirect('workerview')
def workeraddschedule(request):
    form = AppointmentScheduleForm()
    if request.method =='POST':
        form = AppointmentScheduleForm(request.POST)
        if form.is_valid():
            form=form.save(commit=False)
            form.worker=Worker.objects.get(user=request.user)
            form.save()
            return redirect('workerviewschedule')
            messages.info(request,'Schedule Added Successfully')
    return render(request,'WORKER/workeraddschedule.html',{'form':form})

def workerviewschedule(request):
    w = Worker.objects.get(user=request.user)
    wrv = AppointmentSchedule.objects.filter(worker=w)
    context={
        'schedule':wrv
    }
    return render(request,'WORKER/workerviewschedule.html',context)

def customerscheduleview(request):
    cs = AppointmentSchedule.objects.all()
    context = {
        'schedule':cs
    }
    return render(request,'CUSTOMER/scheduleview.html',context)

def scheduleupdate(request,id):
    su = AppointmentSchedule.objects.get(id=id)
    if request.method=='POST':
        form = AppointmentScheduleForm(request.POST or None, instance=su)
        if form.is_valid():
            form.save()
            messages.info(request,'Schedule Updated')
            return redirect('workerviewschedule')
    else:
        form=AppointmentScheduleForm(instance=su)
    return render(request,'WORKER/workerupdateschedule.html',{'form':form})

def scheduledelete(request,id):
    sd = AppointmentSchedule.objects.get(id=id)
    if request.method=='POST':
        sd.delete()
        return redirect('workerviewschedule')

def bookservice(request,id):
    sa = AppointmentSchedule.objects.get(id=id)
    c = Customer.objects.get(user=request.user)
    appointment = AppointmentBooking.objects.filter(user=c,schedule=sa)
    if appointment.exists():
        messages.info(request,'You have already requested for this service')
        return redirect('customerscheduleview')
    else:
        if request.method == 'POST':
            obj = AppointmentBooking()
            obj.user = c
            obj.schedule = sa
            obj.save()
            messages.info(request,'Booked for this service succesfully')
            return redirect('appointmentview')
    return render(request,'CUSTOMER/bookservice.html',{'schedule':sa})

def bookserviceform(request,id):
    bs = AppointmentSchedule.objects.get(id=id)
    if request.method == 'POST':
        form = AppointmentScheduleForm(request.POST or None, instance=bs)
        if form.is_valid():
            form.save()
            messages.info(request,'Service Booking request has been sent')
            return redirect('viewbookedschedule')
    else:
        form = AppointmentScheduleForm(instance=bs)
    return render(request,'CUSTOMER/bookservice.html',{'form':form})


def viewbookedschedule(request):
    c = Customer.objects.get(user=request.user)
    ab = AppointmentBooking.objects.filter(user=c)
    return render(request,'CUSTOMER/viewbookedschedule.html',{'appointment':ab})

def view_bill_user(request):
    u = Customer.objects.get(user=request.user)
    bill = Bill.objects.filter(name=u)
    return render(request,'CUSTOMER/view_bill_user.html',{'bills':bill})

def pay_bill(request,id):
    bi = Bill.objects.get(id=id)
    form = Billpayform()
    if request.method == 'POST':
        card = request.POST.get('card')
        c = request.POST.get('cvv')
        da =request.POST.get('exp')
        CreditCard(card_no=card,card_cvv=c,expiry_date=da).save()
        bi.status = 1
        bi.save()
        messages.info(request,'Bill Paid Successfully')
        return redirect('bill_history')
    return render(request,'CUSTOMER/pay_bill.html',)

def pay_in_direct(request,id):
    bi = Bill.objects.get(id=id)
    bi.status = 2
    bi.save()
    messages.info(request,'Choosed to pay directly in Office')
    return redirect('bill_history')

def bill(request):
    form = Billaddform()
    if request.method == 'POST':
        form = Billaddform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_bill')
    return render(request,'ADMIN/generate_bill.html',{'form':form})

def view_bill(request):
    bill = Bill.objects.all()
    return render(request,'ADMIN/view_payment_details.html',{'bill':bill})

def customerviewbill(request):
    u = Customer.objects.get(user=request.user)
    bill = Bill.objects.filter(user=u)
    return render(request,'CUSTOMER/customerviewbill.html',{'bill':bill})

def pay_bill(request,id):
    bi = Bill.objects.get(id=id)
    form = Billpayform()
    if request.method == 'POST':
        card = request.POST.get('card')
        c = request.POST.get('cvv')
        da = request.POST.get('exp')
        CreditCard(card_no=card, card_cvv=c, expiry_date=da).save()
        bi.status = 1
        bi.save()
        messages.info(request,'Bill Paid Successfully')
        return redirect('customerviewbill')
    return render(request,'CUSTOMER/pay_bill.html',{'form':form})

def custfeedbackadd(request):
    form = FeedbackForm()
    if request.method == 'POST':
        form =FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('custfeedbackview')
    return render(request,'CUSTOMER/custfeedbackadd.html',{'form':form})

def custfeedbackview(request):
    cf = Feedback.objects.all()
    return render(request,'CUSTOMER/custfeedbackview.html',{'cf':cf})

def adminfeedbackview(request):
    af = Feedback.objects.all()
    return render(request,'ADMIN/adminfeedbackview.html',{'af':af})

def feedbackreply(request, id):
    fd = Feedback.objects.get(id=id)
    if request.method == 'POST':
        r = request.POST.get('reply')
        fd.reply = r
        fd.save()
        messages.info(request, 'feedback reply updated')
        return redirect('adminfeedbackview')
    return render(request, 'ADMIN/feedbackreply.html', {'fd': fd})



















