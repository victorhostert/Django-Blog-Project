from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

def signin(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            #TODO: log the user in
            return redirect('blog:home')

    else:
        form = UserCreationForm()

    return render(request, 'accounts/signin.html', {'form': form})

def login(request):
    return render(request, 'accounts/login.html')
