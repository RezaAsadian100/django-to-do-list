from django.shortcuts import render,redirect
from django.contrib import messages 
from users.forms import UserRegistrationForm


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,f'Your account has been created! Login "NOW"')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'users/register.html',{'form':form})            


def profile(request):
    return render(request, 'users/profile.html')