from django.shortcuts import render

# Create your views here.
def applicant_home(request):
    return render(request,'applicantdashboard.html')