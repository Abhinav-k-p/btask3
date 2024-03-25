from django import forms
from .models import Newjob

class Jobform(forms.ModelForm):
    
    class Meta:
        model = Newjob
        fields = ['company_name','jobtitle','jobdescription','qualifications','salary','type','is_available']


  