from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from carparts.models import SparePart

# @login_required
def homepage(request):
    parts = SparePart.objects.all()
    return render(request,'home.html',{"parts": parts})