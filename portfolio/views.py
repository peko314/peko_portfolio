from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'portfolio/home.html')

def secondhome(request):
    return render(request, 'portfolio/home2.html')    
def youtube(request):
    return render(request, 'portfolio/youtube.html')    


