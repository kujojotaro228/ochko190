from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'base.html')
def other(request):
    return render(request, 'other.html')
def other1(request):
    return render(request, 'other1.html')
def other2(request):
    return render(request, 'other2.html')
def other3(request):
    return render(request, 'other3.html')
