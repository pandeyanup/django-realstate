from django.shortcuts import render, redirect
from .models import Listing
from .forms import ListingForm

# Create your views here.

def listings_list(request):
    listings = Listing.objects.all()
    return render(request, 'listings.html', context={'listings': listings})

def listing_retrieve(request, pk):
    listing = Listing.objects.get(id=pk)
    return render(request, 'listing.html', context={'listing': listing})

def listing_create(request):
    form = ListingForm()
    if request.method == 'POST':
        form = ListingForm(request.POST, request.FILES)
        print(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
            
    return render(request, 'listing_create.html', context={'form': form})

def listing_update(request, pk):
    listing = Listing.objects.get(id=pk)
    form = ListingForm(instance=listing)

    if request.method == 'POST':
        form = ListingForm(request.POST, instance=listing, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
            
    return render(request, 'listing_update.html', context={'form': form})

def listing_delete(request, pk):
    listing = Listing.objects.get(id=pk)
    listing.delete()
    return redirect('/')