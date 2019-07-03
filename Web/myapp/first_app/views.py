from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

from listings.choices import price_choices,bedroom_choices,state_choices
from listings.models import Listings
from realtors.models import Realtors

def index(request):
    listings = Listings.objects.order_by('-list_date').filter(is_published= True)[:3]
    context = {
        'listings':listings,
        'state_choices':state_choices,
        'price_choices':price_choices,
        'bedroom_choices':bedroom_choices,
    }
    return render(request,'Pages/index.html',context)


def about(request):
    # get all realtors
    realtors = Realtors.objects.order_by('-hire_date')

    # get seller of month
    mvp_realtors = Realtors.objects.all().filter(is_mvp=True)

    context = {
        'realtors':realtors,
        'mvp_realtors': mvp_realtors

    }
    return render(request,'Pages/about.html',context)
