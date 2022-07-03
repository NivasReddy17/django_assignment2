from django.shortcuts import render
from django.http import HttpResponse
from .forms import userform
def home(request):
    context ={}
    form = userform(request.POST or None, request.FILES or None)
    context['form']= form
    if form.is_valid():
        form.save()
        a=request.POST['name']
        b=request.POST['email']
        c=request.POST['gender']
        d=request.POST['DOB']
        e=request.POST['password']
        return render(request,"display.html",{'name':a,'email':b,'gender':c,'DOB':d,'password':e})
    else:
        return render(request, "index.html",context)
