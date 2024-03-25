from django import forms
from . models import *

class ApplicantDataForm(forms.ModelForm):

    class Meta:
        model = Applicant_data
        fields = ['first_name','last_name','degree','skills','location','resume',]
        
class JobDoneForm(forms.ModelForm):
    class Meta:
        model = Job_apply
        fields = ['name','experience','phonenumber','coverletter','file']