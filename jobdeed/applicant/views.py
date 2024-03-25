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

def viewform(request):
    if request.method == 'POST':
        form = JobDoneForm(request.POST)
        if form.is_valid():
            # Assign the current user as the applicant before saving the form
            job_apply_instance = form.save(commit=False)
            job_apply_instance.applicant = request.user
            job_apply_instance.save()
            return redirect('applicanthome')  # Redirect to success URL after saving
    else:
        form = JobDoneForm()
    return render(request, 'jobapply.html', {'form': form})




    
