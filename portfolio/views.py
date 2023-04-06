from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from .models import Project

# Create your views here.
def home(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/home.html', {'projects': projects})

def project(request, project_id):
    project = Project.objects.get(id=project_id)
    projects = Project.objects.all()
    return render(request, 'portfolio/portfolio.html', {'project': project , 'projects': projects})