from django.shortcuts import render,HttpResponseRedirect
from .forms import MyRegistrationForm
from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth import login,logout,authenticate
from django.urls import reverse


def sign_up(request):
    form = MyRegistrationForm()
    registered = False
    if request.method == "POST":
        form = MyRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            registered = True


    dict = {'form':form,'registered':registered}
    return render(request,'App_Login/signup.html',dict)


def login_page(request):
    form = AuthenticationForm()
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
    return render(request,'App_Login/login.html',{'form':form})
