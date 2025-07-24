from django.shortcuts import render,HttpResponse
from django.contrib import messages
from users.models import UserRegisterModel,StatementsModels

# Create your views here.

def adminlogin(request):
    return render(request,'admins/adminlogin.html',{})

def adminlogincheck(request):
    if request.method == "POST":
        usid = request.POST.get('loginid')
        pswd = request.POST.get('password')
        print("User ID is = ", usid)
        if usid == 'admin' and pswd == 'admin':
            return render(request, 'admins/adminhome.html')
        else:
            messages.success(request, 'Please Check Your Login Details')
    return render(request, 'admins/adminlogin.html')
def activateusers(request):
    dict = UserRegisterModel.objects.all()
    return render(request,'admins/activateusers.html',{'objects':dict})

def activatewaitedusers(request):
    if request.method=='GET':
        id = request.GET.get('uid')
        print('ID is ',id)
        status = 'activated'
        print("PID = ", id, status)
        UserRegisterModel.objects.filter(id=id).update(status=status)
        registerusers = UserRegisterModel.objects.all()
        return render(request, 'admins/activateusers.html', {'objects': registerusers})
def logout(request):
    if request.method=='GET':
        print('Log out Request Came')
        return render(request,'index.html',{})


def viewresults(request):
    dict = StatementsModels.objects.all()
    return render(request,'admins/results.html',{'objects':dict})

