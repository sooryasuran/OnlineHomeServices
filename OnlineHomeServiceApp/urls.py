from django.urls import path

from OnlineHomeServiceApp import views

urlpatterns = [
    path('',views.homeview,name='homeview'),
    path('aboutus',views.aboutus,name='aboutus'),
    path('services',views.services,name='services'),
    path('Contact',views.Contact,name='Contact'),
    path('loginview',views.loginview,name='loginview'),
    path('adminhome',views.adminview,name='adminhome'),
    path('addworker',views.addworker,name='addworker'),
    path('workerview',views.workerview,name='workerview'),
    path('workerhome',views.workerhome,name='workerhome'),
    path('customerview',views.customerview,name='customerview'),
    path('customerregister',views.customerregister,name='customerregister'),
    path('logoutview',views.logoutview,name='logoutview'),
    path('admincustomerview',views.admincustomerview,name='admincustomerview'),
    path('workerslistupdate/<int:id>',views.workerslistupdate,name='workerslistupdate'),
    path('workerdelete/<int:id>',views.workerdelete,name='workerdelete'),
    path('customerhome',views.customerhome,name='customerhome'),
    path('customerscheduleview',views.customerscheduleview,name='customerscheduleview'),
    path('workeraddschedule',views.workeraddschedule,name='workeraddschedule'),
    path('workerviewschedule',views.workerviewschedule,name='workerviewschedule'),
    path('scheduleupdate/<int:id>',views.scheduleupdate,name='scheduleupdate'),
    path('scheduledelete/<int:id>',views.scheduledelete,name='scheduledelete'),
    path('bookservice/<int:id>',views.bookservice,name='bookservice'),
    path('bookserviceform/<int:id>',views.bookserviceform,name='bookserviceform'),
    path('viewbookedschedule',views.viewbookedschedule,name='viewbookedschedule'),
    path('view_bill_user',views.view_bill_user,name='view_bill_user'),
    path('pay_bill',views.pay_bill,name='pay_bill'),
    path('pay_in_direct',views.pay_in_direct,name='pay_in_direct'),
    path('bill',views.bill,name='bill'),
    path('view_bill',views.view_bill,name='view_bill'),
    path('customerviewbill',views.customerviewbill,name='customerviewbill'),
    path('pay_bill/<int:id>',views.pay_bill,name='pay_bill'),
    path('workercustomerview',views.workercustomerview,name='workercustomerview'),
    path('custfeedbackadd',views.custfeedbackadd,name='custfeedbackadd'),
    path('custfeedbackview',views.custfeedbackview,name='custfeedbackview'),
    path('adminfeedbackview',views.adminfeedbackview,name='adminfeedbackview'),



]