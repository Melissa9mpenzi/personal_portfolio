from django.shortcuts import render
from .models import Skill, Service

# Create your views here.

def index(request):
    return render(request, 'port_app/index.html')

def about(request):
    skills = Skill.objects.all()
    return render(request, 'port_app/about.html', {'skills': skills})

def services(request):
    services = Service.objects.all()
    return render(request, 'port_app/services.html', {'services': services})

def resume(request):
    return render(request, 'port_app/resume.html')

def contact(request):
    return render(request, 'port_app/contact.html')
