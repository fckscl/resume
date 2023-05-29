from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'resume/index.html', {'title' : 'Pugach'})

def projects(request):
    return render(request, 'resume/projects.html', {'title' : 'Projects'})

def education(request):
    return render(request, 'resume/education.html', {'title' : 'Education'})

def experience(request):
    return render(request, 'resume/experience.html', {'title' : 'Experience'})

def contacts(request):
    return render(request, 'resume/contacts.html', {'title' : 'Contacts'})