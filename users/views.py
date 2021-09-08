from django.shortcuts import render
from django.contrib.auth import authenticate
from django.http import request
from django.shortcuts import render , redirect
from django.contrib.auth import logout , login
from django.contrib.auth.decorators import login_required
from users.forms import SignUpForm

@login_required(redirect_field_name="next",login_url=None)
def index(request):
    return render(request,'index.html')

@login_required
def dashboard(request):
    return render(request,'dashboard.html')


def register(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        form = SignUpForm()
        context = {'form': form,"title":"Register"}
        return render(request,'registration/register.html',context)

def register_data(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'POST':
            form = SignUpForm(request.POST)
            if form.is_valid():
                form.save()
                email = form.cleaned_data['email']
                name = form.cleaned_data['name']
                password = form.cleaned_data['password1']
                user = authenticate(email=email,password=password)
                print((user))
                print((user.id))
                print(login(request,user))
                return redirect('/')
            else:
                context = {'form': form}
                return render(request,'registration/register.html',context)
        else:
            return redirect('/register')



def logout_view(request):
    logout(request)
    message = {'mes': "You are logout"}
    return render(request,'logout.html',message)
    # return redirect("/accounts/login/")