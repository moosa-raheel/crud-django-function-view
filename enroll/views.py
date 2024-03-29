from django.shortcuts import render
from enroll.form import AddStudentForm
from django.http import HttpResponseRedirect
from enroll.models import Student

# Create your views here.
def show_add(request):
    '''This function will add and show data in template file'''
    if request.method == "POST":
        fm = AddStudentForm(request.POST)
        if fm.is_valid():
            fm.save()
            print(fm.cleaned_data)
        return HttpResponseRedirect("/")
    else:
        fm = AddStudentForm()
        data = Student.objects.all
        return render(request,"show_add.html",{"form":fm,"data":data})
    
def delete(request,id):
    '''This view function will delete data from database'''
    if request.method == "POST":
        Student(pk=id).delete()
        return HttpResponseRedirect("/")
    else:
         return HttpResponseRedirect("/")
    
def update(request,id):
    '''This function will update data from database'''
    data = Student.objects.get(pk=id)
    if request.method == "POST":
       fm = AddStudentForm(request.POST , instance=data)
       if fm.is_valid():   
           fm.save()
        
       return HttpResponseRedirect("/")
    else:
        fm = AddStudentForm(instance=data)
        return render(request,"update.html",{"form":fm})