from django.shortcuts import render
from django.http import HttpResponse

from .models import Departments, Doctors
from .forms import BookingForm
# Create your views here.

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request, 'about.html')

def booking(request):
    if request.method=="POST":
        form=BookingForm(request.POST)
        if form.is_valid():
            form.save()
    form=BookingForm()
    dict_form={
        'form':form
    }
    return render(request,'booking.html',dict_form)

def departments(request):
    dict_dep={
        'dep': Departments.objects.all()
    }
    return render(request,'departments.html',dict_dep)

def contact(request):
    return render(request,'contact.html')

def doctors(request):
    dict_doc={
        'doc':Doctors.objects.all()
    }
    return render(request,'doctors.html',dict_doc)