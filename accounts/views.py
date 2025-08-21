from django.shortcuts import render, redirect
from .forms import UserRegistration, LoginForm, UserEditForm, ProfileEditForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
# Create your views here.

def registerUser(request):
    if request.method == 'POST':
        form = UserRegistration(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.email = user.email.lower()
            user.set_password(
                form.cleaned_data['password']
            )
            user.save()
            return redirect('login')
        
    else:
        form = UserRegistration(request.POST)
    # form = UserRegistration()
    return render(request,'accounts/registerUser.html',{'form':form})


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                request,
                username = cd['username'],
                password = cd ['password']
            )
            if user is not None:
                login(request,user)
                messages.success(request, "Welcome back, {user.username}")
                return redirect("home")
            
            else: 
                messages.error(request,"Invalid username or password")
    else:
        form = LoginForm()
    return render(request,"accounts/login.html",{"form": form})


def edit(request):
    if request.method == 'POST':
        userform = UserEditForm(
            instance=request.user,
            data= request.POST
        )
        profileform = ProfileEditForm(
            instance=request.user.profile,
            data=request.POST,
            files= request.FILES
        )
        if userform.is_valid() and profileform.is_valid():
            userform.save()
            profileform.save()

        else: 
            userform = UserEditForm(instance=request.user)
            profileform = ProfileEditForm(instance=request.user.profile)

        return render(request,'accounts/edit.html',{
            'userform':userform,
            'profileform':profileform
        })