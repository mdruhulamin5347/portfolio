from django.shortcuts import render,redirect
from django.contrib import messages
from .models import *
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def HOME(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subjectt = request.POST.get('subject')
        message = request.POST.get('message')
        obj = ContactModel(name=name, email=email, subject=subjectt, message=message)
        obj.save()
        subject = 'Portfolio Contact Form Submission'
        message = f'You have received a new message from: {name}\n Email:({email}):\n Subject: {subjectt} \n Message: {message}'
        email_from = f'{email}'
        recipient_list = [settings.EMAIL_HOST_USER]  # Replace with your desired recipient email
        send_mail(subject, message, email_from, recipient_list)
        messages.success(request, "Your message has been sent successfully.")
        return redirect('home')
    carousol = CarouselModel.objects.first()
    workdetails = WorkDetails.objects.first()
    aboutme = AboutMeModel.objects.first()
    myskill = MySkillModel.objects.all()
    services = ServicesModel.objects.all()
    projects = ProjectModel.objects.all()
    context ={
        'carousol':carousol,
        'workdetails':workdetails,
        'aboutme':aboutme,
        'myskill':myskill,
        'services':services,
        'projects':projects
    }
    return render(request,'home.html',context)