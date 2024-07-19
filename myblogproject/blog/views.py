from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import BlogEntry
from .forms import BlogEntryForm


def index(request):
    entries =BlogEntry.objects.all()
    return render(request, 'blog/index.html', {'entries': entries})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')
        else: 
            form = UserCreationForm()
        return render(request, 'blog/signup.html', {'form': form})
    
def login_view(request):
    if request.methood == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        return render(request, 'blog/login.html')
    
def logout_view(request):
    logout(request)
    return redirect('index')

@login_required
def create_entry(request):
    if request.method == 'POST':
        form = BlogEntryForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.author = request.user
            entry.save()   
            return redirect('index')
        else:
            form = BlogEntryForm()
        return render(request, 'blog/create_entry.html', {'form' : form})    