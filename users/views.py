from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST) # creates form that contains the POST data
        if form.is_valid(): # if data is valid, no errors
            form.save() # saves the account and hashes the password
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account Created! You can now login!')
            return redirect('login')
    else:
        form = UserRegisterForm() # creates a blank form and renders to the template
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'users/profile.html')
