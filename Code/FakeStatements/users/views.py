from django.shortcuts import render
from django.contrib import messages
from .models import UserRegisterModel,StatementsModels

from .statementcleaning import preprocess_tweet
from .algorithm import prediction
import random
import csv
from django.conf import settings
from .algorithm import classifier


# Create your views here.
def userlogin(request):
    return render(request,'users/UserLogin.html',{})

def userregister(request):
    return render(request,'UserRegister.html',{})

def userRegisterAction(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        username = request.POST.get('username')
        mobile = request.POST.get('mobile')
        dob = request.POST.get('dob')
        gender = request.POST.get('gender')
        address = request.POST.get('address')
        status = 'waiting'
        try:
            obj = UserRegisterModel.objects.create(email=email,password=password,username=username,mobile=mobile,dob=dob,gender=gender,address=address,status=status)
            print(obj.id)
            if( obj.id > 0):
                messages.success(request, 'You have been successfully registered')
                print('user Register Success')
            else:
                messages.success(request, 'Email Already Registerd')
                print('user Already exist')
        except:
            messages.success(request, 'Email Already Registerd please change new mail')
            pass
    return render(request, 'UserRegister.html', {})

def userlogincheck(request):
    if request.method == "POST":
        usremail = request.POST.get('usremail')
        pswd     = request.POST.get('password')

        try:
            check    = UserRegisterModel.objects.get(email=usremail,password=pswd)
            request.session['id'] = check.id
            #print('User Email ', usremail, ' password is ', pswd)
            request.session['loggeduser'] = check.username
            request.session['email'] = check.email
            status = check.status
            if status == "activated":
                print("User id At", check.id, status)
                return render(request, 'users/userhomepage.html')
            else:
                messages.success(request, 'Your Account Not at activated')
                return render(request, 'users/UserLogin.html')
        except:
            pass
        messages.success(request, 'Invalid Email id and password')
        return render(request, 'users/UserLogin.html')

def userwritestatements(request):
    return render(request,'users/writestatements.html',{})

def userstatementrecord(request):
    if request.method == 'POST':
        statemnt = request.POST.get('statement')
        cleanedstatement = preprocess_tweet(statemnt)
        print('Cleaned Statement ',cleanedstatement)
        rsltdict = prediction.detecting_fake_news(cleanedstatement)
        label = rsltdict['label']
        score = rsltdict['score']
        probscore = round(score, 2)
        #print('The Statement is ==',label,'Probability Score is = ',score)
        csvHeader = 'Statement,Label'
        csvData = cleanedstatement+",%s" % label
        csvd = [[csvHeader],[csvData]]
        with open(settings.MEDIA_ROOT + "\\" +'test.csv',mode='w') as csvFile:
            writer = csv.writer(csvFile, delimiter=',')
            writer.writerow(['Statement', 'Label'])
            writer.writerow([cleanedstatement, str(label)])

        csvFile.close()
        dictScore = classifier.runAlgorithm()
        print("Rama Dict is ",dictScore)
        thestatmentis = ""

        dict = {'statement':cleanedstatement,'label':label,'probabilityscore':probscore}
        logisticregression = dictScore['LogicRegressionClassification']
        username = request.session['loggeduser']
        email = request.session['email']
        StatementsModels.objects.create(email=email,username=username,statement=cleanedstatement,label=label,probscore=probscore,logisticregression=100*logisticregression)
        dbdict = StatementsModels.objects.all()
		#SELECT statement, COUNT(statement) AS value_occurrence   FROM  statementresults   GROUP BY statement  ORDER BY value_occurrence DESC;

    #print(dbdict)
    return render(request,'users/resultofstatement.html',{'dict':dict,'objects':dbdict})