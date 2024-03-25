from django.db import models
from jobdeedapp.models import Users

# Create your models here.

class Newjob(models.Model):
    company_name = models.CharField(max_length=100)
    jobtitle = models.CharField(max_length=100)
    jobdescription = models.TextField()
    qualifications = models.CharField(max_length=100)
    salary = models.PositiveIntegerField()
    type = models.CharField(max_length=100)
    is_available = models.BooleanField()
    user = models.ForeignKey(Users,on_delete=models.CASCADE,  related_name='jobs')
   