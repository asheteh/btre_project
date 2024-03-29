from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator,EmptyPage
from .models import Listings
from listings.choices import price_choices,bedroom_choices,state_choices

def index(request):
    # order by used to show most recent home 1st
    listings = Listings.objects.order_by('-list_date').filter(is_published=True)

    paginator = Paginator(listings,6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)



    context  ={
        'listings':paged_listings
    }
    return render(request,'listings/listing.html',context)


def listing(request,listing_id):
    listing = get_object_or_404(Listings,pk=listing_id)
    context ={
        'listing':listing
    }
    return render(request,'listings/listings.html',context)


def search(request):

    queryset_list =  Listings.objects.order_by('-list_date')

    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(description__icontains = keywords)
       
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list = queryset_list.filter(city__iexact = city)
    
    #lte is less than eqyual to
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_list = queryset_list.filter(bedrooms__lte = bedrooms)

    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(price__lte = price)

    context = {
        'state_choices':state_choices,
        'price_choices':price_choices,
        'bedroom_choices':bedroom_choices,
        'listings':queryset_list,
        'values' : request.GET
    }
    return render(request,'listings/search.html',context)

