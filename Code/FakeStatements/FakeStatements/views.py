from django.shortcuts import render

def index(request):
    return render(request,'index.html',{})

def logout(request):
    if request.method=='GET':
        print('Log out Request Came')
        return render(request,'index.html',{})