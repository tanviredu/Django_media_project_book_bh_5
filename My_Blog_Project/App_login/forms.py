from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class MyRegistrationForm(UserCreationForm):
    def __init__(self,*args,**kargs):
        super(MyRegistrationForm,self).__init__(*args,**kargs)
        self.fields['username'].widget.attrs = {'class': 'form-control',}
        self.fields['password1'].widget.attrs = {'class': 'form-control',}
        self.fields['password2'].widget.attrs = {'class': 'form-control',}

        #if you need any additional field
        # you can add here 
        class Meta:
            model = User
            fields = ('username','password1','password2')
