from django.http import HttpResponse

def index(request):
    return HttpResponse("i am home page")
