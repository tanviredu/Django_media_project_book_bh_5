from django.shortcuts import render,HttpResponseRedirect
from .forms import MyRegistrationForm,UserProfileChange
from django.contrib.auth.forms import AuthenticationForm

# need separate form for changing password

from django.contrib.auth.forms import PasswordChangeForm



from django.contrib.auth import login,logout,authenticate
from django.urls import reverse

from django.contrib.auth.decorators import login_required

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


@login_required
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required
def profile(request):
    return render(request,'App_Login/profile.html',{})



@login_required
def user_change(request):
    current_user = request.user
    form = UserProfileChange(instance=current_user)
    if request.method == "POST":
        current_data = request.POST
        form = UserProfileChange(current_data,instance=current_user)
        if form.is_valid():
            form.save()
            # render with newly information
            form = UserProfileChange(instance=current_user)



    return render(request,'App_Login/change_profile.html',context={'form':form})

@login_required
def pass_change(request):
    current_user = request.user
    form = PasswordChangeForm(current_user)
    if request.method == "POST":
        form = PasswordChangeForm(current_user,data=request.POST)
        if form.is_valid():
            form.save()
            

    return render(request,"App_login/change_pass.html",{'form':form})
