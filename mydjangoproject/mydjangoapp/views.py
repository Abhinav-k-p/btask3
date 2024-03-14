from django.shortcuts import render
from django.views.generic import ListView,DetailView
from . models import Movie,Dirdetails

# Create your views here.
def movie_list(request):
    movie_info = Movie.objects.all()
    return render(request, 'movielist.html',{'movie_info':movie_info})

def moviedetails(request,pk):
    movie_details=Movie.objects.get(pk=pk)
    context = {
        'movie' : movie_details
        }
    return render(request, 'moviedetails.html',context)


class Dirlist(ListView):
    model=Dirdetails
    template_name='dirlist.html'
    context_object_name='directors'



class Dirdetails(DetailView):
    model=Dirdetails
    template_name='dirdetails.html'
    context_object_name='director'
    
    

    