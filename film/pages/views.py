
from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import F,Q
from django.utils import timezone

# Create your views here.
from .decorators import *
from .models import *
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage

# Create your views here.
def error(request):
    return render(request,'pages/404.html')
def about(request):
    return render(request,'pages/about.html')
    
def catalog1(request):
    film=Film.objects.all()
    cartoons=Film.objects.filter(category__name='cartoons')
    movies=Film.objects.filter(category__name='movies')

    p=Paginator(film,2)
    page_num=request.GET.get('page')
    
    try:
        page=p.page(page_num)
    
    except PageNotAnInteger:
        page=p.page(1)

    except EmptyPage:
        page=p.page(1)

    kate={'film':page, 'cartoons':cartoons,'movies':movies}
    return render(request,'pages/catalog1.html',kate)


def catalog2(request):
    return render(request,'pages/catalog2.html')
def details1(request,id):
    film=Film.objects.get(id=id)
    return render(request,'pages/details1.html',{'film':film})

    
def details2(request,id):
    series=Film.objects.get(id=id)
    episode=Episode.objects.filter(season__film__id=id)
    seasons=Season.objects.filter(film__id=id)
    allseasons=[]
    for season in seasons:
        dic={}
        dic["number"]=season.season_number
        dic["episode"]=season.episode_set.all()
        allseasons.append(dic)
    print(allseasons)

    return render(request,'pages/details2.html',{'series':series,'episode':episode,"you":allseasons})
def faq(request):
    return render(request,'pages/faq.html')


@ authenticate
def index(request):
    film=Film.objects.all()
    cartoons=Film.objects.filter(category__name='cartoons')

    series=Film.objects.filter(category__name='tvseries')

    movies=Film.objects.filter(category__name='movies')

    kate={'film':film, 'cartoons':cartoons,'movies':movies,'series':series}
   
    return render(request,'pages/index.html',context=kate)
def index2(request):
    return render(request,'pages/index2.html')
def pricing(request):
    return render(request,'pages/pricing.html')

def new(request):
    context = {"image": Episode.episode_name }
    
def addNew(request):
    # get the first user
    user = User.objects.get(id=1)
    #get the all groups that exists in
    group = user.group_set.all()
    make = User.objects.filter(name__icontains="kenny")
    # get the query set that name field contains kenny OR lade
    #       1. the querysearch is case - insensitive
    fade = Group.objects.filter(Q(name__icontains="kenny") & Q(name__icontains="lade"))
    print(group,"🐛")
    print(make,"👩‍🍳")
    print(fade,'🐵')
    return HttpResponse("<body>hello world everyone</body>")


