from django.shortcuts import render, get_object_or_404
from .models import Movies, category
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError



# Create your views here.
def home(request):
    Category = category.objects
    
    return render(request, 'Home/home.html',{'category': Category})

def addmovie(request):
    return render(request, 'Home/addmovie.html')

def submission(request):
    if request.method == 'POST':
        print("hooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo")
        Names= request.POST['MovieName']
        image = request.FILES['image']
        Subtitles = request.POST['subtitle']
        Directors = request.POST['director']
        Genres = request.POST['genre']
        Reviews = request.POST['review']
        Categorys = request.POST['category']
        movieinfo = Movies(Name=Names,Image=image,Subtitle=Subtitles,Director=Directors,Genre=Genres,Review=Reviews, Category=category.objects.get(id=Categorys))
        movieinfo.save()

    return render(request, 'Home/addmovie.html')

def detail(request, movie_id):
    movies = get_object_or_404(Movies.objects, pk=movie_id)
    return render(request, 'Home/detail.html', {'detail':movies})


def Categorys(request, cat_id):
    #Category = get_object_or_404(category.objects, pk=cat_id)
    Category = category.objects.get(id=cat_id)
    return render(request, 'Home/category.html',{'categorys':Category})



