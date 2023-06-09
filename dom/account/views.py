

# Create your views here.
from django.shortcuts import render,redirect
from pages.views import * 
from .forms import *
from django.contrib.auth import authenticate,login,logout
from django.core.mail import send_mail, EmailMessage
from django.conf import settings
# Create your views here.
def view1(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,
                     password=password)
        if user is not None:
            login(request,user)
            return redirect(index)



    return render(request,'account/signin.html')



def view2(request):
    form=Contactform()
    if request.method=='POST':
        # contact=Contact(email=request.POST.get('email'),name=request.POST.get('username'),
        #                 phonenumber=request.POST.get('phonenumber'),
        #                 message=request.POST.get('message'))
        form  =Contactform(request.POST)
        if form.is_valid():
            form.save()
            return redirect(view1)
        else:
            f = Contactform()
            messages.add_message(request,messages.ERROR,"your credentials is wrong")


    kate={'form':form}
    return render(request,'account/signup.html',context=kate)

def man(request):
    logout(request) 
    return redirect(view1)

def test_cookie(request):   
    if not request.COOKIES.get('color'):
        response = HttpResponse("Cookie Set")
        response.set_cookie('color', 'blue')
        return response
    else:
        return HttpResponse("Your favorite color is {0}".format(request.COOKIES['color']))


def send_email_to_client():
    subject = 'Welcome to our website'
    message = 'Hope you are enjoying your stay'
    from_email = settings.EMAIL_HOST_USER
    recipient_list = ['kennyokhamena@gmail.com',]
    send_email(subject, message, from_email, recipient_list)
    
def send_email_attachment(subject,  message, from_email, recipient_list, attachment):
    mail =EmailMessage( subject=subject, body=message, from_email=from_email, to=recipient_list)
    mail.send()
    
def send_home(request):
    subject = 'Welcome to our website'
    message = 'Hope you are enjoying your stay'
    from_email = settings.EMAIL_HOST_USER
    recipient_list = ['kennyokhamena@gmail.com',]
    send_email_attachment(subject=subject, message=message, from_email=from_email, recipient_list=recipient_list, attachment='static/images/1.jpg')