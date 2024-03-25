from django.urls import path,include
from.import views 
 
urlpatterns = [
    path("",views.recruiter_home,name='recruiterhome'),
    path("Jobcreate/",views.Jobcreate,name='Jobcreate'),
    path("applicantview/",views.applicantview,name='applicantview'),
    
]