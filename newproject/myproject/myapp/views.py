from django.shortcuts import render,redirect
from myapp.models import dep,emp
# /ad/de/d
# Create your views here.
def landing(req):
        if 'admin_e' in req.session and 'admin_p' in req.session:
          a_data = {
            'email': req.session['admin_e'],
            'password': req.session['admin_p'],
            'name': req.session['admin_n']
        }
          return render(req,'landing.html', {'data': a_data})
        else:
             return render(req,'landing.html')


def login(req):
    if req.method == 'POST':
        e = req.POST.get('email')
        p = req.POST.get('password')
        if e == 'admin@gmail.com' and p == 'admin':
            req.session['admin_e'] = e
            req.session['admin_p'] = p
            req.session['admin_n'] = 'admin'
            return redirect('admindpanel')
        else:
            x={'g':"wrong passord or username"}
            return render(req,'login.html',{'data':x})

    return render(req, 'login.html')

def admindpanel(req):
    # Admin Session Check
    if 'admin_e' in req.session and 'admin_p' in req.session:
        a_data = {
            'email': req.session['admin_e'],
            'password': req.session['admin_p'],
            'name': req.session['admin_n']
        }
        deptdata=dep.objects.all()
        all_emp=emp.objects.all()
        return render(req, 'admindpanel.html', {'data': a_data,'deptdata':deptdata,'all_emp':all_emp})
    else:
        return redirect('login')
    


def logout(req):
    if 'admin_e' in req.session:
        req.session.flush()
        return redirect('landing')
    else:
        return redirect('login')
   

def about(req):
       if 'admin_e' in req.session and 'admin_p' in req.session:
        a_data = {
            'email': req.session['admin_e'],
            'password': req.session['admin_p'],
            'name': req.session['admin_n']
        }
        return render(req,'about.html', {'data': a_data})
       else:
            return render(req,'about.html')

def services(req):
        if 'admin_e' in req.session and 'admin_p' in req.session:
         a_data = {
            'email': req.session['admin_e'],
            'password': req.session['admin_p'],
            'name': req.session['admin_n']
        }
         return render(req,'services.html', {'data': a_data})
        else:
            return render(req,'services.html')



def sin(req):
          if 'admin_e' in req.session and 'admin_p' in req.session:
           a_data = {
            'email': req.session['admin_e'],
            'password': req.session['admin_p'],
            'name': req.session['admin_n']
        }
           return render(req,'sin.html', {'data': a_data})
          else:
               return render(req,'sin.html')
 

def free(req):
            if 'admin_e' in req.session and 'admin_p' in req.session:
             a_data = {
            'email': req.session['admin_e'],
            'password': req.session['admin_p'],
            'name': req.session['admin_n']
        } 
             return render(req,'free.html', {'data': a_data})
            else:
                 return render(req,'free.html')

def xbox(req):
         if 'admin_e' in req.session and 'admin_p' in req.session:
          a_data = {
            'email': req.session['admin_e'],
            'password': req.session['admin_p'],
            'name': req.session['admin_n']
        }
          return render(req,'xbox.html', {'data': a_data})
         else:
              return render(req,'xbox.html')

# form wala
def save_department(req):
    if req.method=='POST':
          dname=req.POST.get('dept_name')
          dcode=req.POST.get('dept_code')
          dhead=req.POST.get('dept_head')
          dbudget=req.POST.get('dept_budget')
          ddesc=req.POST.get('dept_desc')
          deptdata=dep.objects.filter(dept_name=dname)
          if not deptdata:
            dep.objects.create(dept_name=dname,dept_code=dcode,dept_head=dhead,dept_budget=dbudget,dept_desc=ddesc)
            return redirect("add_department")
          else:
            return redirect('add_department')
     
    return redirect('login')

def addemp(req):
        if 'admin_e' in req.session and 'admin_p' in req.session:
            a_data = {
                    'email': req.session['admin_e'],
                    'password': req.session['admin_p'],
                    'name': req.session['admin_n']
                } 
            if req.method=='POST':
                fname=req.POST.get('fname')
                lname=req.POST.get('lname')
                email=req.POST.get('email')
                img=req.FILES.get('img')
                adhaar=req.FILES.get('adhaar')
                code=req.POST.get('code')
                mobile=req.POST.get('mobile')
                DOB=req.POST.get('DOB')
                gender=req.POST.get('gender')
                edu=req.POST.getlist('edu')
                dept=req.POST.get('dept')
                user=emp.objects.filter(code=code)
                al=dep.objects.all()
                if user :
                    deptdata=dep.objects.all()
                    return render(req,'admindpanel.html', {'data': a_data,"add_employees":True,'deptdata':deptdata})
                if not al.exists():
                    deptdata=dep.objects.all()
                    return render(req,'admindpanel.html', {'data': a_data,"add_employees":True,'deptdata':deptdata})
                else:
                     
                    emp.objects.create(fname=fname,lname=lname,email=email,img=img,adhaar=adhaar,code=code,mobile=mobile,DOB=DOB,gender=gender,edu=edu,dept=dept)
                    deptdata=dep.objects.all()
                    return render(req,'admindpanel.html', {'data': a_data,"add_employees":True,'deptdata':deptdata})
        else:
            return redirect('login')


# buttons wale
def add_anlytics(req):
    if 'admin_e' in req.session and 'admin_p' in req.session:
          a_data = {
            'email': req.session['admin_e'],
            'password': req.session['admin_p'],
            'name': req.session['admin_n']
        }
          return render(req,'admindpanel.html', {'data': a_data,'add_anlytics':True})
    else:
        msg={'msg':'login first'}
        return render(req,"login.html",{'msg':msg})

def  add_setting(req):
    if 'admin_e' in req.session and 'admin_p' in req.session:
          a_data = {
            'email': req.session['admin_e'],
            'password': req.session['admin_p'],
            'name': req.session['admin_n']
        }
          return render(req,'admindpanel.html', {'data': a_data,'add_setting':True})
    else:
        msg={'msg':'login first'}
        return render(req,"login.html",{'msg':msg})


def  add_employees(req):
    if 'admin_e' in req.session and 'admin_p' in req.session:
          a_data = {
            'email': req.session['admin_e'],
            'password': req.session['admin_p'],
            'name': req.session['admin_n']
        }
         
          deptdata=dep.objects.all()
          return render(req,'admindpanel.html', {'data': a_data,"add_employees":True,'deptdata':deptdata})
    

    else:
        msg={'msg':'login first'}
        return render(req,"login.html",{'msg':msg})

def  all_employees(req):
    if 'admin_e' in req.session and 'admin_p' in req.session:
          a_data = {
            'email': req.session['admin_e'],
            'password': req.session['admin_p'],
            'name': req.session['admin_n']
        }
          all_emp = emp.objects.all()
          return render(req,'admindpanel.html', {'data': a_data,"all_employees":True,'all_emp':all_emp})
    else:
        msg={'msg':'login first'}
        return render(req,"login.html",{'msg':msg})

def  remove_employees(req):
    if 'admin_e' in req.session and 'admin_p' in req.session:
          a_data = {
            'email': req.session['admin_e'],
            'password': req.session['admin_p'],
            'name': req.session['admin_n']
        }
          return render(req,'admindpanel.html', {'data': a_data,"remove_employees":True})
    else:
        msg={'msg':'login first'}
        return render(req,"login.html",{'msg':msg})

def  remove_department(req):
    if 'admin_e' in req.session and 'admin_p' in req.session:
          a_data = {
            'email': req.session['admin_e'],
            'password': req.session['admin_p'],
            'name': req.session['admin_n']
        }
          return render(req,'admindpanel.html', {'data': a_data,"remove_department":True})
    else:
        msg={'msg':'login first'}
        return render(req,"login.html",{'msg':msg})


def add_department(req):
    if 'admin_e' in req.session and 'admin_p' in req.session:
          a_data = {
            'email': req.session['admin_e'],
            'password': req.session['admin_p'],
            'name': req.session['admin_n']
        }
          return render(req,'admindpanel.html', {'data': a_data,"add_department":'add_department'})
    else:
        msg={'msg':'login first'}
        return render(req,"login.html",{'msg':msg})
    
 

def all_department(req):
        if 'admin_e' in req.session and 'admin_p' in req.session:
          a_data = {
            'email': req.session['admin_e'],
            'password': req.session['admin_p'],
            'name': req.session['admin_n']
        }
          deptdata=dep.objects.all()
          return render(req,'admindpanel.html', {'data': a_data,"all_department":True,'deptdata':deptdata})
    
        else:
         msg={'msg':'login first'}
         return render(req,"login.html",{'msg':msg})
    
def all_quries(req):
    if 'admin_e' in req.session and 'admin_p' in req.session:
          a_data = {
            'email': req.session['admin_e'],
            'password': req.session['admin_p'],
            'name': req.session['admin_n']
        }
          return render(req,'admindpanel.html', {'data': a_data,"all_quries":True})
    else:
        msg={'msg':'login first'}
        return render(req,"login.html",{'msg':msg})
    
def payroll(req):
    if 'admin_e' in req.session and 'admin_p' in req.session:
          a_data = {
            'email': req.session['admin_e'],
            'password': req.session['admin_p'],
            'name': req.session['admin_n']
        }
          return render(req,'admindpanel.html', {'data': a_data,"payroll":True})
    else:
        msg={'msg':'login first'}
        return render(req,"login.html",{'msg':msg})
    


    


     



          
          

  