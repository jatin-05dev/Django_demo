from django.shortcuts import render,redirect
from myapp.models import user
from django.contrib import messages
import random

from django.core.mail import send_mail


# Create your views here.
def register(req):
   return render(req,'register.html')

def home2(req):
   return render(req,'home.html')
def home(req):
   if 'email' in req.session and 'password' in req.session:
        a_data = {
            'email': req.session['email'],
            'password': req.session['password'],
        }
        return render(req,'home.html',{'data':a_data})
   else:
      messages.error(req,'login first')
      return redirect('home2')


def about(req):
   if 'email' in req.session and 'password' in req.session:
        a_data = {
            'email': req.session['email'],
            'password': req.session['password'],
        }
        return render(req,'home.html',{'data':a_data})
   else:
      messages.error(req,'login first')
      return redirect('login')
 

def login(req):
   return render(req,'login.html')


def registerfrm(req):
    if req.method=='POST':
      name=req.POST.get('name')
      email=req.POST.get('email')
      password=req.POST.get('password')
      cpassword=req.POST.get('cpassword')
      if cpassword==password:
         use=user.objects.filter(email=email)
         if use:
            messages.error(req,'email alreasy exists')
            return redirect('register')
         else:
            user.objects.create(name=name,email=email,password=password,cpassword=cpassword)
            send_mail(
                    "testing from django",
                    f'hello {email} your added as a employee at microsoft your password',
                    "jattfact@gmail.com",
                    [email],
                    fail_silently=False,
                    )

            return redirect("login")
      else:
         messages.error(req,'password not mathces')
         return redirect('register')
    else:
       return redirect('register')
        

def loginfrm(req):
   if req.method=='POST':
      email=req.POST.get('email')
      password=req.POST.get('password')
      use=user.objects.filter(email=email)
      if use:
         useinfo=user.objects.get(email=email)
         if useinfo.email==email and useinfo.password==password:
            req.session['email']=email
            req.session['password']=password
            
            return redirect('home')
         else:
            messages.error(req,'email no match with password')
            return redirect('login')
      else:
         messages.error(req,'invlaid email')
         return redirect('login')
   else:
      return redirect('login')
    

def logout(req):
   if 'email' in req.session and 'password' in req.session:
      req.session.flush()
      return redirect('register')
   else:
      return redirect('login')
         
def fp(req):
   return render(req,'fp.html')

def fpfrm(req):
   if req.method=='POST':
      email=req.POST.get("email")
      ue=user.objects.filter(email=email)
      if ue:
         u=user.objects.get(email=email)
         if str(u.email)==str(email):
            otp=random.randint(1111,9999)
            req.session['otp']=otp
            req.session['email']=email
            send_mail(
                  subject="Forget password",
                  message=f'User Email OTP: {otp}',
                  from_email="jattfact@gmail.com",  
                  recipient_list=[email],
                  fail_silently=False,
            )
            req.session.set_expiry(60)   # 1 minute
            return redirect('otp')
      else:
         messages.error(req,"thse email is not valid in databases")
         return redirect('fp')
   return render(req, 'fp.html')
   

def otp(req):
   return render(req,'otp.html')

def otpv(req):
   if req.method=='POST': 
      otp=req.POST.get('otp')
      sotp=req.session.get('otp')
      if str(otp)==str(sotp):
        email=req.session.get('email')
        return render(req,'cp.html',{'email':email})
      else:
         messages.error(req,'invalid')
         return redirect('otp')
   email=req.session.get(req,'email')
   return render('cp.html',{'email':email})
   
def cp(req):
   return render(req,'cp.html')



def cpfrm(req):
   if req.method=='POST':
      email=req.POST.get('email')
      np=req.POST.get('np')
      cnp=req.POST.get('cnp')
      if np==cnp:
         use=user.objects.get(email=email)
         use.password=np
         use.cpassword=np
         use.save()
         messages.info(req,"passwoed reset")
         req.session.pop('otp')
         return redirect('home')
      else:
         messages.error(req,'np and cp not match')
         return render(req,'cp.html',{'email':email})
   else:
      return render(req,'cp.html',{'email':email})






        



