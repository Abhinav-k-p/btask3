
from django.shortcuts import render

# Create your views here.
def recruiter_home(request):
    return render(request,'recruiterdashboard.html')