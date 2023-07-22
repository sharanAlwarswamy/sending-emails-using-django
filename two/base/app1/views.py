from django.shortcuts import render
from app1.models import app1_customer
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.


def index(request):
    return render(request,'email.html')


def sendMail(request):
    # if request.method == 'Post':
    firstName = request.POST['firstName']
    secondName = request.POST['secondName']
    email = request.POST['email']
    message = request.POST['comment']
    
        #got data from frontend 
    courtesy = "ThankYou for your feedback :) \n Will get in touch shortly"
    message = "~~'\n" + message + "\n'~~" + " \n \n \n " + courtesy
    # querry = app1_customer(firstName=firstName,secondName=secondName,email=email,message=message)
    # querry.save()

        # saved to db
    print(firstName +"  "+ secondName)
    send_mail(
        'Feedback Form', #subject of the mail
        message,
        'sharanalwar57@gmail.com', # email addr of sender present in settings.py file
        [email], #recievers mailID
        fail_silently = False
        )
        #send to mail

    return render(request , 'submit.html')
