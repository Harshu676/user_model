from django.shortcuts import render

# Create your views here.

from app.forms import *


def Topic_Form(request):
    form=TopicForm()
    if request.method=='POST':
        form_data=TopicForm(request.POST)
        if form_data.is_valid():
            form_data.save()

    return render(request,'Topic_form.html',context={'form':form})


def Webpage_Form(request):
    form=WebpageForm()
    if request.method=="POST":
        form_data=WebpageForm(request.POST)
        if form_data.is_valid():
            form_data.save()

    return render(request,'webpage_form.html',context={'form':form})