from django.shortcuts import render
from django.http import HttpResponse
from projects.models import Project

# Create your views here.

def project_list(request):
    return render(request, 'projects/index.html')


def all_projects(request):
    # query the db to return all project objects
    projects = Project.objects.all()
    
    # drukuje w konsoli po każdym uruchomieniu widoku w przeglądarce
    print(projects[0].title)

    # w plikac template mamy dostęp do danych poprzez zadeklarowaną wartość 'projects
    return render(request, 'projects/all_projects.html', {'projects': projects})


def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    return render(request, 'projects/project_detail.html', {'project': project})

