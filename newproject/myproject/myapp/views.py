from django.shortcuts import render,redirect

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


def lo(req):
    if req.method == 'POST':
        e = req.POST.get('email')
        p = req.POST.get('password')
        if e == 'admin@gmail.com' and p == 'admin':
            req.session['admin_e'] = e
            req.session['admin_p'] = p
            req.session['admin_n'] = 'admin'
            return redirect('admindashboard')
        else:
            x={'g':"wrong passord or username"}
            return render(req,'lo.html',{'data':x})

    return render(req, 'lo.html')

def admindashboard(req):
    # Admin Session Check
    if 'admin_e' in req.session and 'admin_p' in req.session:
        a_data = {
            'email': req.session['admin_e'],
            'password': req.session['admin_p'],
            'name': req.session['admin_n']
        }
        return render(req, 'admindashboard.html', {'data': a_data})
    else:
        return redirect('lo')
    


def logout(req):
    if 'admin_e' in req.session:
        req.session.flush()
        return redirect('landing')
    else:
        return redirect('lo')
   

def tr(req):
       if 'admin_e' in req.session and 'admin_p' in req.session:
        a_data = {
            'email': req.session['admin_e'],
            'password': req.session['admin_p'],
            'name': req.session['admin_n']
        }
        return render(req,'tr.html', {'data': a_data})
       else:
            return render(req,'tr.html')

def o(req):
        if 'admin_e' in req.session and 'admin_p' in req.session:
         a_data = {
            'email': req.session['admin_e'],
            'password': req.session['admin_p'],
            'name': req.session['admin_n']
        }
         return render(req,'o.html', {'data': a_data})
        else:
            return render(req,'o.html')



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

def x(req):
         if 'admin_e' in req.session and 'admin_p' in req.session:
          a_data = {
            'email': req.session['admin_e'],
            'password': req.session['admin_p'],
            'name': req.session['admin_n']
        }
          return render(req,'x.html', {'data': a_data})
         else:
              return render(req,'x.html')



  