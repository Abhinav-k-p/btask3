from django.db import models
from jobdeedapp.models import *
from recruiter.models import *

# Create your models here.

class Applicant_data(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    skills = models.CharField(max_length=100)  
    location = models.CharField(max_length=100)
    resume = models.FileField(upload_to='resume/')
    
class Job_apply(models.Model):
    name = models.CharField(max_length=100)
    experience = models.PositiveIntegerField()
    phonenumber = models.PositiveIntegerField()
    coverletter = models.TextField(max_length=100)
    file = models.FileField(upload_to='recruiter/resume/')
    job = models.ForeignKey(Newjob,on_delete=models.CASCADE,related_name='job')
    applicant = models.ForeignKey(Users, on_delete=models.CASCADE,related_name='application')
    
    
    
    
