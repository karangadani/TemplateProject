from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'index.html')

def common(request):
    return render(request,'commom.html')