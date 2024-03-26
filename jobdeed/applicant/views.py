from django.shortcuts import render,redirect
from .forms import *
from recruiter.models import *

# Create your views here.
def applicant_home(request):
    job = Newjob.objects.all()
    return render(request,'applicantdashboard.html',{'job': job})

def edit(request):
    editform = ApplicantDataForm()
    if request.method == 'POST':
        editform = ApplicantDataForm(request.POST,request.FILES)
        if editform.is_valid():
            edit = editform.save(commit=False)
            edit.user = request.user
            edit.save()
            return redirect('viewprofile')
    else:
        editform = ApplicantDataForm()
        
    return render(request,'applicantregister.html',{'editform': editform})

def viewprofile(request):
    data = Applicant_data.objects.get(user=request.user)
    return render(request,'applicantprofile.html',{'data':data})

# def viewform(request):
#     viewform = JobDoneForm()
#     if request.method == 'POST':
#         viewform = JobDoneForm(request.POST,request.FILES)
#         if viewform.is_valid():
#             edit = viewform.save(commit=False)
#             edit.user = request.user
#             edit.save()
#             return redirect('applicanthome')
#     else:
#         viewform = JobDoneForm()
        
#     return render(request,'jobapply.html',{'viewform': viewform})

def viewform(request, job_id):
    job = get_object_or_404(Newjob, pk=job_id)
    if request.method == 'POST':
        viewform = JobDoneForm(request.POST, request.FILES)
        if viewform.is_valid():
            job_apply_instance = viewform.save(commit=False)
            job_apply_instance.applicant = request.user  # Assuming applicant_id corresponds to user
            job_apply_instance.job = job
            job_apply_instance.save()
            job_seekeremail = request.user.email
            subject = f"job application for {job.jobtitle}"
            message = f"Application for this job is submitted succesfully send"
            send_mail(subject,message,settings.EMAIL_HOST_USER,[job_seekeremail])
            recruiter_mail = job.user.email
            subject = f"job application {job.jobtitle}"
            message = f"{request.user.username} is applied for {job.jobtitle}"
            send_mail(subject,message,settings.EMAIL_HOST_USER,[recruiter_mail])
            return redirect('applicanthome')
    else:
        viewform = JobDoneForm()
        
    return render(request, 'jobapply.html', {'viewform': viewform})




    
