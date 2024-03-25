from django.urls import path,include
from.import views 
 
urlpatterns = [
    path("",views.applicant_home,name='applicanthome'),
    
 
]