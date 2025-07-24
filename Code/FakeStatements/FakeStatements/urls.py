"""FakeStatements URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import index,logout
from admins.views import adminlogin,adminlogincheck,activateusers,activatewaitedusers,viewresults
from users.views import userlogin,userregister,userRegisterAction,userlogincheck,userwritestatements,userstatementrecord
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name='index'),
    path('logout',logout,name='logout'),


    path('adminlogin',adminlogin,name='adminlogin'),
    path('adminlogincheck',adminlogincheck,name='adminlogincheck'),
    path('activateusers',activateusers,name='activateusers'),
    path('activatewaitedusers',activatewaitedusers,name='activatewaitedusers'),
    path('viewresults',viewresults,name='viewresults'),



    path('userRegisterAction',userRegisterAction,name='userRegisterAction'),
    path('userlogin',userlogin,name='userlogin'),
    path('userregister',userregister,name='userregister'),
    path('userlogincheck',userlogincheck,name='userlogincheck'),
    path('userwritestatements',userwritestatements,name='userwritestatements'),
    path('userstatementrecord',userstatementrecord,name='userstatementrecord'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)