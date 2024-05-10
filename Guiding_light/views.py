from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def contact(request):
    return render(request,'contact.html')
def appointment(request):
    return render(request,'appointment.html')

def features(request):
    return render(request,'features.html')

def testimonial(request):
    return render(request,'testimonial.html')