from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

def signin(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            #TODO log in the user
            form.save()
            return redirect('blog:home')

    else:
        form = UserCreationForm()

    return render(request, 'accounts/signin.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            #TODO log in the user
            return redirect('blog:home')

    else:
        form = AuthenticationForm()

    return render(request, 'accounts/login.html', {'form': form})

    #TODO Django tutorial #22 - 0:00
