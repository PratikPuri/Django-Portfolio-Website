from django.shortcuts import redirect, render
from .models import Education, Project, Skill, Message
from .forms import MessageForm,feedbackForm
from django.contrib import messages
import sys, json
sys.path.append("..")
from api.serializers import FeedbackSerializer
import requests;

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

def feedbackPage(request):
    form = feedbackForm()
    if request.method == 'POST':
        # print (request);
        # print (request.POST);
        # print (request.POST.get('rating'));
        # print (request.POST.get('body'));
        # request.data = {'rating':request.POST.get('rating'),'body':request.POST.get('body')};
        # print (request.body.decode('utf-8'));
        # print (json.loads(request.body))
        data1 = {'rating':request.POST.get('rating'),'body':request.POST.get('body')};
        requests.post(request.build_absolute_uri('/addFeedbackData'), json=data1)
        messages.success(request,'Thank you for your feedback!');
        return redirect('/');
    else:
        return render(request,'base/feedback.html',{'form':form});