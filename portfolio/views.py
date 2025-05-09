from django.shortcuts import render

from .models import Profile, Stat
from .models import Summary, Education, Experience
from .forms import ContactForm

# Create your views here.
def index(request):
    form = ContactForm()
    return render(request, 'index.html', {'form': form})



def home(request):
    #contact form database
    # if request.method == 'POST':
    #     name == request.POST['name']
    #     email == request.POST['email']
    #     subject == request.POST['subject']
    #     message == request.POST['message']
    #     contact = models.Home(name=name, email=email, subject=subject, message=message)
    #     contact.save()
    return render(request, 'home.html')


def project(request):
    return render(request, 'project.html')

def contact_view(request):
    success = False
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            success = True
            form = ContactForm()  # Reset form after successful submit
    else:
        form = ContactForm()
    return render(request, 'index.html', {'form': form, 'success': success})