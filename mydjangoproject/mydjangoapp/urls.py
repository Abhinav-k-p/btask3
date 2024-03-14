from django.urls import path
from .import views 

urlpatterns = [
    
    path('movielist',views.movie_list,name = 'movielist'),
    path('moviedetails/<int:pk>',views.moviedetails,name = 'moviedetails'),
    path('dirlist',views.Dirlist.as_view(),name = 'dirlist'),
    path('dirdetails/<int:pk>',views.Dirdetails.as_view(),name = 'dirdetails'),
]