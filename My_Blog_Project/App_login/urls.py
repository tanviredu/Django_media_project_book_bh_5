from django.urls import path
from . import views
app_name = "App_login"
urlpatterns = [
    path('signup/',views.sign_up,name='sign_up'),
    path('login/',views.login_page,name='login'),
]
