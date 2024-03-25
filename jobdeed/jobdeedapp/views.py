from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import SignupForm
from . models import *



def registeration(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

        else:
            print(form.errors)
    else:
        form = SignupForm()
        return render(request, 'user_signup.html', {'form': form})
    # return render(request,'signup.html')


def loginuser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request, user)
            if user.user_type == 'RECRUITER':
                return render(request, 'recruiterdashboard.html')
            else:
                return redirect('applicanthome')
        else:
            return render(request,'user_login.html')
    return render(request, 'user_login.html')

