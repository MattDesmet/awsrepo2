from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'awsapp/index.html')

def page2(request):
    return render(request, 'awsapp/page2.html')
