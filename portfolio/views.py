from django.shortcuts import render

from .models import Profile, Stat
from .models import Summary, Education, Experience
from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.
def index(request):
    form = ContactForm()
    return render(request, 'index.html', {'form': form})



# def home(request):
#     #contact form database
#     # if request.method == 'POST':
#     #     name == request.POST['name']
#     #     email == request.POST['email']
#     #     subject == request.POST['subject']
#     #     message == request.POST['message']
#     #     contact = models.Home(name=name, email=email, subject=subject, message=message)
#     #     contact.save()
#     return render(request, 'home.html')


def project(request):
    return render(request, 'project.html')


def contact_view(request):
    success = False
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            # Send email to site owner
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            send_mail(
                subject=f"New Contact Message: {subject}",
                message=f"From: {name} <{email}>\n\n{message}",
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[settings.EMAIL_HOST_USER],
                fail_silently=False,
            )
            success = True
            form = ContactForm()
    else:
        form = ContactForm()

    return render(request, 'index.html', {'form': form, 'success': success})