from django.shortcuts import render
from .forms import UserRegistration
# Create your views here.

def registerUser(request):
    # if request.method == 'POST':
    #     form = UserRegistration(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return 
        
    # else:
    #     form = UserRegistration(request.POST)
    form = UserRegistration()
    return render(request,'accounts/registerUser.html',{'form':form})