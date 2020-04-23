from django.conf import settings
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from django.contrib import messages
from .forms import DonorForm, ReceiverForm

from .models import *
# Create your views here.
def home(request):
    return render(request, 'organdonate/home.html')

def donor(request):
    return render(request, 'organdonate/donor.html')

def receiver(request):
    return render(request, 'organdonate/receiver.html')

def ad(request):
    return render(request, 'organdonate/ad.html')

def eye(request):
    return render(request,'organdonate/eye.html')

def eye2(request):
    return render(request,'organdonate/eye2.html')

def heart(request):
    return render(request,'organdonate/heart.html')

def heart2(request):
    return render(request,'organdonate/heart2.html')

def kidney(request):
    return render(request,'organdonate/kidney.html')

def kidney2(request):
    return render(request,'organdonate/kidney2.html')

def lungs(request):
    return render(request,'organdonate/lungs.html')

def lungs2(request):
    return render(request,'organdonate/lungs2.html')

def more_info(request):
    return render(request,'organdonate/more_info.html')

def more_info2(request):
    return render(request,'organdonate/more_info2.html')

def about_us(request):
    return render(request,'organdonate/about_us.html')


def ad(request):
    donor = Donor.objects.all()
    
    return render(request,'organdonate/ad.html',{'donor':donor})

def eyedonor(request):
    donor = Donor.objects.all()
    return render(request,'organdonate/eyedonor.html',{'donor':donor})

def lungsdonor(request):
    donor = Donor.objects.all()
    return render(request,'organdonate/lungsdonor.html',{'donor':donor})

def kidneydonor(request):
    donor = Donor.objects.all()
    return render(request,'organdonate/kidneydonor.html',{'donor':donor})

def heartdonor(request):
    donor = Donor.objects.all()
    return render(request,'organdonate/heartdonor.html',{'donor':donor})

def eyeReceiver(request):
    receiver = Receiver.objects.all()
    return render(request,'organdonate/eyeReceiver.html',{'receiver':receiver})

def heartReceiver(request):
    receiver = Receiver.objects.all()
    return render(request,'organdonate/heartReceiver.html',{'receiver':receiver})

def lungsReceiver(request):
    receiver = Receiver.objects.all()
    return render(request,'organdonate/lungsReceiver.html',{'receiver':receiver})

def kidneyReceiver(request):
    receiver = Receiver.objects.all()
    return render(request,'organdonate/kidneyReceiver.html',{'receiver':receiver})

def register(request):
    form = DonorForm()
    if request.method =='POST':
        form = DonorForm(request.POST)
        organ = request.POST.get('organ')
        name = request.POST.get('name')
        email = request.POST.get('email')
        
        #print("Organ is @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@", organ, "Name ==============", name)
        #print("MY Form is like this-------------------------------",form)
        if form.is_valid():
            form.save()
            # send_mail(subject, message, from_email, to_list, fail_silently= False)
            subject = 'Thank You So Much For Your Registration!!!!'
            message1 = 'Dear '+name+'\n\n '+'We are really Thankful to you that you showed this kind Gesture of donation your '+organ+'.'
            message2 = ' Your this kind gesture can save the life of some unknown and blessings given by them will surely be helpful to you in the situation when you will need them the most.'
            message3 = '\n\n\n Regards \n\n Crystal Shine Donation'
            message = message1+message2+message3
            from_email = settings.EMAIL_HOST_USER
            to_list= [email]

            send_mail(subject, message, from_email, to_list, fail_silently= False)

            messages.success(request,'Your Donation in succesfully accepted')
            donor = Donor.objects.all()
            if organ == 'Kidney':
                return redirect('kidneydonor')
            if organ == 'Lungs':
                return redirect('lungsdonor')
            if organ == 'Eyes':
                return redirect('eyedonor')
            if organ == 'Heart':
                return redirect('heartdonor')
                

    return render(request,'organdonate/register.html',{'form':form})

def registration(request):
    form = ReceiverForm()
    if request.method =='POST':
        form = ReceiverForm(request.POST)
        organ = request.POST.get('organ')
        name = request.POST.get('name')
        email = request.POST.get('email')
        
        #print("Organ is @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@", organ, "Name ==============", name)
        #print("MY Form is like this-------------------------------",form)
        if form.is_valid():
            form.save()
            
            subject = 'We Have Registered Your request for Organ'
            
            message = 'Dear '+ name +'\n\n\n'+'We have registered your request for your '+organ+' We will soon reach to you as soon as we get the donor for '+ organ+'\n\n'+ 'Regards'+'\n CrystalShine Donation'
            from_email = settings.EMAIL_HOST_USER
            to_list= [email]

            send_mail(subject, message, from_email, to_list, fail_silently= False)
            if organ == 'Kidney':
                return redirect('kidneydonor')
            if organ == 'Lungs':
                return redirect('lungsdonor')
            if organ == 'Eyes':
                return redirect('eyedonor')
            if organ == 'Heart':
                return redirect('heartdonor')
    return render(request,'organdonate/registration.html',{'form':form})




























def delete(request,pk):
    donor = Donor.objects.get(id = pk)
    if request.method == "POST":
        order.delete()
        return redirect('home')

    return render(request,'organdonate/register.html',{'form':form})


   
def heart(request):
    return render(request,'organdonate/heart.html')

def lungs(request):
    return render(request,'organdonate/lungs.html')

def kidney(request):
    return render(request,'organdonate/kidney.html')