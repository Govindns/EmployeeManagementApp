from django.shortcuts import render,redirect
from .models import Employee
from .forms import EmpForm

def list(requset):
    emp=Employee.objects.all()
    return render(requset,'testapp/home.html',{'emp':emp})

def post(request):
    form=EmpForm()
    if request.method=='POST':
        form=EmpForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request,'testapp/post.html',{'form':form})


def put(request,id):
    emp=Employee.objects.get(id=id)
    form=EmpForm(instance=emp)
    if request.method=='POST':
        form=EmpForm(request.POST,instance=emp)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request, 'testapp/put.html', {'form':form})

def delete(request,id):
    emp=Employee.objects.get(id=id).delete()
    return redirect('/')

def about(request):
    return render(request,'testapp/about.html')