from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
from truelines.models import RegisterTable, QuotesPost


def Index_page(request):
    all=QuotesPost.objects.all()
    return render(request,"htmlpages/index.html",{"data":all})
def Login_page(request):
    return render(request, "htmlpages/login.html")
def Register_page(request):
    return render(request, "htmlpages/register.html")
def Data_Register(request):
    msg=""
    if request.method =="POST":
        username=request.POST['username']
        mobileno=request.POST['mobileno']
        email=request.POST['email']
        password=request.POST['password']

        user=RegisterTable(username=username,mobileno=mobileno,email=email,password=password)
        user.save();
        msg="User Registered Successfully"
        return render(request,"htmlpages/login.html",{"msg":msg})
    else:
        msg="NOT SAVED"
    return render(request,"htmlpages/register.html")
def Data_Login(request):
    if request.method=="POST":

        mobileno=request.POST["mobileno"]
        password=request.POST["password"]
        try:
            if RegisterTable.objects.get(mobileno=mobileno,password=password )is not None:
                request.session['mobileno']=mobileno
                x=RegisterTable.objects.get(mobileno=mobileno)
                all=QuotesPost.objects.all()
                i = QuotesPost.objects.filter(topic__startswith='INSPIRATIONAL')
                f = QuotesPost.objects.filter(topic__startswith='FEEL')
                m = QuotesPost.objects.filter(topic__startswith='MOTI')
                r = QuotesPost.objects.filter(topic__startswith='RELA')
                fa = QuotesPost.objects.filter(topic__startswith='FAMO')
                s = QuotesPost.objects.filter(topic__startswith='SEAS')
                c = QuotesPost.objects.filter(topic__startswith='CULT')
                ro = QuotesPost.objects.filter(topic__startswith='ROMA')
                return render(request,"htmlpages/index1.html",{"mobileno":mobileno,'data':x,"all":all,"ins":i,'feel':f,'moti':m,'rela':r,'famo':fa,'seas':s,'cult':c,'roma':ro})
        except:
            msg="Invalid User "
            return render(request,"htmlpages/login.html",{"msg":msg})

    return render(request, "htmlpages/login.html")
def Data_Logout(request):
    try:
        del request.session['mobileno']
    except:
        pass
    return redirect("Login_page")
def My_account(request):
    mobileno= request.session['mobileno']
    x = RegisterTable.objects.get(mobileno=mobileno)
    return render(request,"htmlpages/myaccount.html",{"mobileno":mobileno,'data':x})
def Update_account(request,id):
    s=RegisterTable.objects.get(id=id)
    return render(request, "htmlpages/updateaccount.html", {"data":s})
def Do_Update(request,id):
    if request.method=="POST":
        up=RegisterTable.objects.get(id=id)
        up.username=request.POST['username']
        up.email = request.POST['email']
        up.password = request.POST['password']
        up.save()
        msg="User Updated"
        return redirect("My_account")
    else:
        msg="User Not Updated"
        return render(request,"htmlpages/updateaccount.html",{"msg":msg})
def Write_Quotes(request):
    mobileno= request.session['mobileno']
    x = RegisterTable.objects.get(mobileno=mobileno)
    return render(request,"htmlpages/writequotes.html",{"data":x})

def Quotes_Post(request):
    msg = ""
    if request.method == "POST":
        topic = request.POST['topic']
        quotes = request.POST['quotes']
        mobileno = request.POST['mobileno']
        username = request.POST['username']

        user = QuotesPost(topic=topic,quotes=quotes,mobileno=mobileno,username=username)
        user.save();
        request.session['mobileno'] = mobileno
        mobileno = request.session['mobileno']
        x = RegisterTable.objects.get(mobileno=mobileno)
        msg = "Your Quotes Posted Successfully"
        return render(request, "htmlpages/writequotes.html", {"msg": msg,"data":x})
    else:
        msg = "NOT POSTED TRY AGAIN"
    return render(request, "htmlpages/writequotes.html")

def My_Quotes(request):
    mobileno = request.session['mobileno']
    x = RegisterTable.objects.get(mobileno=mobileno)
    y= QuotesPost.objects.filter(mobileno=mobileno)
    return render(request,"htmlpages/myquotes.html",{"data":x,"quotes":y})
def Delete_Post(request,id):
    b = QuotesPost.objects.get(id=id)
    b.delete()
    return redirect("My_Quotes")
def Home_page(request):
    x=QuotesPost.objects.all()
    return render(request,"htmlpages/index.html",{"data":x})