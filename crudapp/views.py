from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import student
from django.contrib import messages


# Create your views here.
#Home Page
def home(request):
    data = student.objects.all()
    return render(request, "home.html", {'data': data})

#To save data in database
def save(request):
    if request.method == "POST":
        id = request.POST['id']
        fname = request.POST['fname']
        _class = request.POST['class']
        address = request.POST['address']
        x=student(id=id, fullname=fname,Class=_class,address=address)
        x.save()
        messages.success(request, "Data stored successfully")
    else:
        return HttpResponseRedirect("404 Not found")
    return redirect("/")

#To delete data 
def delete(request):
    id = request.GET['id']
    student.objects.filter(id = id).delete()
    messages.success(request, "Data deleted successfully")
    return redirect("/")

#To Edit data
def edit(request):
    id = request.GET['id']
    for data in student.objects.filter(id=id):
        fname = data.fullname
        _class = data.Class
        address = data.address
        return render(request,"show.html", { 'id':id, 'fullname':fname, 'Class':_class, 'address':address})

#For data Edit successfully
def recordedited(request):
    if request.method == 'POST':
        id = request.POST['id']
        fname = request.POST['fname']
        _class = request.POST['class']
        address = request.POST['address']
        student.objects.filter(id=id).update(fullname=fname, Class= _class, address=address)
        messages.success(request, "Data updated successfully")
        return redirect("/")
    else:
        return HttpResponseRedirect("404 Not found")

