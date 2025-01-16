from django.shortcuts import render
from .models import Skill, Service

# Create your views here.

def index(request):
    return render(request, 'core/index.html')

def about(request):
    skills = Skill.objects.all()
    return render(request, 'core/about.html', {'skills': skills})

def services(request):
    services = Service.objects.all()
    return render(request, 'core/services.html', {'services': services})

def resume(request):
    return render(request, 'core/resume.html')

def contact(request):
    return render(request, 'core/contact.html')
