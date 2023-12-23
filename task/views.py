from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.forms import UserCreationForm
from .models import *
from .forms import *

# Create your views here.


def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('list')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User do not exist!!')
            
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('list')    
        else:
            messages.error(request,'User name OR Password do not exist')    
            
    context = {'page': page}
    return render(request, 'task/login_register.html', context)


def logoutUser(request):
    logout(request)
    return redirect('list')


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('list')
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username
            user.save()
            login(request, user)
            return redirect('list')
        else:
            messages.error(request,'Problem during Registre') 
    return render(request, 'task/login_register.html',{'form': form})
            
            

def index(request):
    if request.user.is_authenticated:
        # Get tasks for the current logged in user
        tasks = Task.objects.filter(user=request.user)
    else:
        tasks = Task.objects.none()  # No tasks if user is not authenticated

    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
        return redirect('/')
    
    context = { 'tasks': tasks, 'form': form} 
    return render(request, 'task/list.html', context)

    
    
"""
def index(request):
    tasks = Task.objects.filter(user=request.user)
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    context = { 'tasks': tasks, 'form': form} 
    return render(request, 'task/list.html', context) """
            
        




@login_required(login_url='login')
def updateTask(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'task/update_task.html', context)



@login_required(login_url='login')
def delete(request, pk):
    item = Task.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('/')
    context = {"item": item}
    return render(request, 'task/delete.html', context)


def about(request):
    return render(request, 'task/about.html')
    


