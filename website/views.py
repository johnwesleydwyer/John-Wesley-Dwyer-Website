from django.shortcuts import render
from django.core.mail import send_mail
import os

apps_email = os.environ.get("APPS_EMAIL")
apps_pass = os.environ.get("APPS_PASSWORD")

def index(request):

    if request.method == 'POST':
        inputName = request.POST['inputName']
        inputEmail = request.POST['inputEmail']
        inputMessage = request.POST['inputMessage']

        send_mail(
            inputName + " | Website Request",
            inputMessage,
            inputEmail,
            [apps_email],
        )

        send_mail(
            "John Wesley Dwyer",
            "Thank you for your message! I will respond as quickly as possible!",
            apps_email,
            [inputEmail],
        )

        return render(request, 'index.html', {'inputName': inputName})

    else:
        return render(request, 'index.html', {})
