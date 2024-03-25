
from django.shortcuts import render,get_object_or_404
from .forms import Jobform
from .models import *
from applicant.models import *


# Create your views here.
def recruiter_home(request):
    jobs = Newjob.objects.filter(user=request.user)
    return render(request,'recruiterdashboard.html',{'jobs': jobs})


def Jobcreate(request):
    jobform = Jobform()
    if request.method == 'POST':
        jobform = Jobform(request.POST)
        if jobform.is_valid():
            job = jobform.save(commit=False)
            job.user = request.user
            job.save()
            return recruiter_home(request)
    else:
        jobform = Jobform()
    return render(request,'recruiterjob.html',{'jobform':jobform})

def applicantview(request,job_id):
    job = get_object_or_404(Newjob,pk=job_id,user=request.user)
    print(job)
    applicants = Job_apply.objects.filter(job=job)
    
    return render(request,'viewappliedapplicants.html',{'job': job,'user':applicants})



    
    
    

