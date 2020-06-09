from django.shortcuts import render
from .forms import MyRegistrationForm

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
