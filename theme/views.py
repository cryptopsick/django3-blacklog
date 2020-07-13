from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage,\
                                  PageNotAnInteger

from .models import Band, Album
# Create your views here.


def home_page(request):
    bands = Band.objects.all()
    albums = Album.objects.order_by("-added").all()
    paginator = Paginator(albums, 4) # 3 posts in each page
    page = request.GET.get('page')
    try:
        albums = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        albums = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        albums = paginator.page(paginator.num_pages)
    return render (request, 'index.html', {'bands':bands,'albums': albums})
