from django.shortcuts import redirect,render
from django.contrib.auth import login,logout,authenticate
from .forms import CreateUserForm
# Create your views here.

def register_view(request):
    if request.user.is_authenticated:
        return redirect('home:index') 
    else: 
        form = CreateUserForm()
        if request.method=='POST':
            form = CreateUserForm(request.POST)
            if form.is_valid() :
                user=form.save()
                return redirect('accounts:login')
        context={
            'form':form,
        }
        return render(request,'accounts/register.html',context)
 
def login_view(request):
    if request.user.is_authenticated:
        return redirect('home:index')
    else:
       if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
       context={}
       return render(request,'accounts/login.html',context)
 
def logout_view(request):
    logout(request)
    return redirect('/')