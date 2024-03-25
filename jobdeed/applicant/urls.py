from django.urls import path,include
from.import views 
 
urlpatterns = [
    path("",views.applicant_home,name='applicanthome'),
    path("edit/",views.edit,name='edit'),
    path("viewprofile/",views.viewprofile,name='viewprofile'),
    path("viewjobform/",views.viewform,name='viewjobform'),
    
    
 
]