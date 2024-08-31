from django.shortcuts import render
from .models import StudentDb
# Create your views here.
# 
def home(request):
    data=StudentDb.objects.all()
    print(data)
    context={"data": data}
    return render(request, "home.html", context)

def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")
def insertData(request):   
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        age=request.POST.get('age')
        gender=request.POST.get('age')
        query=StudentDb(name=name, email=email, age=age, gender=gender)
        query.save()
        
    return render(request, "home.html")


def updateData(request, id):
    data=StudentDb.objects.get(id=id)
    context={"id": id}
    return render(request, "edit.html", context)

def deleteData(request, id):
    data=StudentDb.objects.all()
    print(data)
    context={"data": data}
    return render(request, "deleteData.html", context)

