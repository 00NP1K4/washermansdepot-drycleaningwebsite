from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import ContactForm, ScheduleForm
from django.contrib import messages
from django.conf import settings

remail ='washermansdepot@gmail.com'
# Create your views here.
def index(request):
    testimonials = Testimonial.objects.all()
    images = Home_Carousel.objects.all()
    steps = Step.objects.all()
    certs = Cert.objects.all()
    services = Service.objects.all()
    if request.method == 'POST':
        sform = ScheduleForm(request.POST)
        if sform.is_valid():
            # send email code goes here
            sender_name = sform.cleaned_data['name']
            sender_email = sform.cleaned_data['email']
            subject = 'Pickup'
            message = "{0} Schedule a pickup!\n\nADDRESS : {1}\n\nSERVICE : {2}\n\nPHONE NUMBER : {3}".format(sender_name, sform.cleaned_data['address'],sform.cleaned_data['service'],sform.cleaned_data['phone'])
            send_mail(subject, message, settings.EMAIL_HOST_USER, [remail], fail_silently=False)
            messages.success(request, 'Message was sent successfully!')
            return redirect('/')
    else:
        sform = ScheduleForm()
    context = {
        'testimonials' :testimonials ,
        'images':images,
        'steps':steps,
        'certs':certs,
        'services':services,
        'sform':sform,
    }
    return render(request, 'washerman/index.html', context)

def commercial(request):
    carousels = Carousel.objects.all()
    QQs = QuickQuotePrice.objects.all()
    dcs = DryAndComm.objects.all()
    certs = Cert.objects.all()
    if request.method == 'POST':
        sform = ScheduleForm(request.POST)
        if sform.is_valid():
            # send email code goes here
            sender_name = sform.cleaned_data['name']
            sender_email = sform.cleaned_data['email']

            subject = 'Pickup'
            message = "{0} Schedule a pickup!\n\nADDRESS : {1}\n\nSERVICE : {2}\n\nPHONE NUMBER : {3}".format(sender_name, sform.cleaned_data['address'],sform.cleaned_data['service'],sform.cleaned_data['phone'])
            send_mail(subject, message, settings.EMAIL_HOST_USER, [remail], fail_silently=False)
            messages.success(request, 'Message was sent successfully!')
            return redirect('/')
    else:
        sform = ScheduleForm()
    context = {
        'carousels':carousels,
        'QQs':QQs,
        'dcs':dcs,
        'certs':certs,
        'sform':sform,
    }
    return render(request, 'washerman/comercial.html', context)

def drycleaning(request):
    steps = Step.objects.all()
    carousels = Carousel.objects.all()
    QQs = QuickQuotePrice.objects.all()
    dcs = DryAndComm.objects.all()
    if request.method == 'POST':
        sform = ScheduleForm(request.POST)
        if sform.is_valid():
            # send email code goes here
            sender_name = sform.cleaned_data['name']
            sender_email = sform.cleaned_data['email']

            subject = 'Pickup'
            message = "{0} Schedule a pickup!\n\nADDRESS : {1}\n\nSERVICE : {2}\n\nPHONE NUMBER : {3}".format(sender_name, sform.cleaned_data['address'],sform.cleaned_data['service'],sform.cleaned_data['phone'])
            send_mail(subject, message, settings.EMAIL_HOST_USER, [remail], fail_silently=False)
            messages.success(request, 'Message was sent successfully!')
            return redirect('/')
    else:
        sform = ScheduleForm()
    context = {
        'steps':steps,
        'carousels':carousels,
        'QQs':QQs,
        'dcs':dcs,
        'sform':sform,
    }
    return render(request, 'washerman/drycleaning.html', context)

def laundromat(request):
    carousels = Carousel.objects.all()
    laundromats = Laundromat.objects.all()
    if request.method == 'POST':
        sform = ScheduleForm(request.POST)
        if sform.is_valid():
            # send email code goes here
            sender_name = sform.cleaned_data['name']
            sender_email = sform.cleaned_data['email']

            subject = 'Pickup'
            message = "{0} Schedule a pickup!\n\nADDRESS : {1}\n\nSERVICE : {2}\n\nPHONE NUMBER : {3}".format(sender_name, sform.cleaned_data['address'],sform.cleaned_data['service'],sform.cleaned_data['phone'])
            send_mail(subject, message, settings.EMAIL_HOST_USER, [remail], fail_silently=False)
            messages.success(request, 'Message was sent successfully!')
            return redirect('/')
    else:
        sform = ScheduleForm()
    context = {
        'carousels':carousels,
        'laundromats':laundromats,
        'sform':sform,
    }
    return render(request, 'washerman/laundromat.html', context)

def schedule(request):
    contacts = Contact.objects.all()
    if request.method == 'POST':
        sform = ScheduleForm(request.POST)
        if sform.is_valid():
            # send email code goes here
            sender_name = sform.cleaned_data['name']
            sender_email = sform.cleaned_data['email']

            subject = 'Pickup'
            message = "{0} Schedule a pickup!\n\nADDRESS : {1}\n\nSERVICE : {2}\n\nPHONE NUMBER : {3}".format(sender_name, sform.cleaned_data['address'],sform.cleaned_data['service'],sform.cleaned_data['phone'])
            send_mail(subject, message, settings.EMAIL_HOST_USER, [remail], fail_silently=False)
            messages.success(request, 'Message was sent successfully!')
            return redirect('/')
    else:
        sform = ScheduleForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # send email code goes here
            sender_name = form.cleaned_data['name']
            sender_email = form.cleaned_data['email']

            subject = 'Contact'
            message = "{0} has sent you a new message:\n\nMESSAGE : {1}".format(sender_name, form.cleaned_data['message'])
            send_mail(subject, message, settings.EMAIL_HOST_USER, [remail], fail_silently=False)
            messages.success(request, 'Message was sent successfully!')
            return redirect('/schedule')
    else:
        form = ContactForm()
    context = {
        'contacts' :contacts ,
        'form' :form,
        'sform':sform,
    }
    return render(request, 'washerman/schedule.html', context)

def price(request):
    prices = Price.objects.all()
    if request.method == 'POST':
        sform = ScheduleForm(request.POST)
        if sform.is_valid():
            # send email code goes here
            sender_name = sform.cleaned_data['name']
            sender_email = sform.cleaned_data['email']

            subject = 'Pickup'
            message = "{0} Schedule a pickup!\n\nADDRESS : {1}\n\nSERVICE : {2}\n\nPHONE NUMBER : {3}".format(sender_name, sform.cleaned_data['address'],sform.cleaned_data['service'],sform.cleaned_data['phone'])
            send_mail(subject, message, settings.EMAIL_HOST_USER, [remail], fail_silently=False)
            messages.success(request, 'Message was sent successfully!')
            return redirect('/')
    else:
        sform = ScheduleForm()
    context = {
        'prices' :prices ,
        'sform':sform,
    }
    return render(request, 'washerman/prices.html', context)

def about(request):
    certs = Cert.objects.all()
    abouts = About.objects.all()
    if request.method == 'POST':
        sform = ScheduleForm(request.POST)
        if sform.is_valid():
            # send email code goes here
            sender_name = sform.cleaned_data['name']
            sender_email = sform.cleaned_data['email']

            subject = 'Pickup'
            message = "{0} Schedule a pickup!\n\nADDRESS : {1}\n\nSERVICE : {2}\n\nPHONE NUMBER : {3}".format(sender_name, sform.cleaned_data['address'],sform.cleaned_data['service'],sform.cleaned_data['phone'])
            send_mail(subject, message, settings.EMAIL_HOST_USER, [remail], fail_silently=False)
            messages.success(request, 'Message was sent successfully!')
            return redirect('/')
    else:
        sform = ScheduleForm()
    context = {
        'certs':certs,
        'abouts':abouts,
        'sform':sform,
    }
   
    return render(request, 'washerman/about.html', context)

def contact(request):
    contacts = Contact.objects.all()
    if request.method == 'POST':
        sform = ScheduleForm(request.POST)
        if sform.is_valid():
            # send email code goes here
            sender_name = sform.cleaned_data['name']
            sender_email = sform.cleaned_data['email']

            subject = 'Pickup'
            message = "{0} Schedule a pickup!\n\nADDRESS : {1}\n\nSERVICE : {2}\n\nPHONE NUMBER : {3}".format(sender_name, sform.cleaned_data['address'],sform.cleaned_data['service'],sform.cleaned_data['phone'])
            send_mail(subject, message, settings.EMAIL_HOST_USER, [remail], fail_silently=False)
            messages.success(request, 'Message was sent successfully!')
            return redirect('/')
    else:
        sform = ScheduleForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # send email code goes here
            sender_name = form.cleaned_data['name']
            sender_email = form.cleaned_data['email']
            subject = 'Contact'
            message = "{0} has sent you a new message:\n\nMESSAGE : {1}".format(sender_name, form.cleaned_data['message'])
            send_mail(subject, message, settings.EMAIL_HOST_USER, [remail], fail_silently=False)
            messages.success(request, 'Message was sent successfully!')
            return redirect('/contact')
    else:
        form = ContactForm()
    context = {
        'contacts' :contacts ,
        'form' :form,
        'sform':sform,
    }
    return render(request, 'washerman/contact.html', context)