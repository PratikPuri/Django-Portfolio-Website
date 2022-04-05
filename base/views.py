from django.shortcuts import redirect, render
from .models import Education, Project, Skill, Message
from .forms import MessageForm

from django.contrib import messages

# Create your views here.

def homepage(request):
    projects = Project.objects.all();
    skills = Skill.objects.all();
    schools = Education.objects.all();
    form = MessageForm()
    if request.method == 'POST':
        form = MessageForm(request.POST);
        form.save();
        form = MessageForm();
        messages.success(request,'Thank you, your message has been delivered successfully!');
    return render(request,'base/home.html',{'projects':projects,'skills':skills,'form':form,'schools':schools});

def inboxPage(request):
    messages = Message.objects.all();
    return render(request,'base/inbox.html',{'messages':messages});

def projectPage(request,pk):
    project = Project.objects.get(id=pk);
    return render(request,'base/project.html',{'project':project});