from django.shortcuts import render
from . forms import RestaurantForm,ReviewForm
from .models import Restaurant, Review
from rest_framework import viewsets
from api.serializers import RestaurantSerializer,ReviewSerializer


# Create your views here.
def index(request):
    restaurants = Restaurant.objects.all()
    form = RestaurantForm()
    dict_Rest ={
        'form': form,
        'restaurants': restaurants
    }
    return render(request, 'index.html', dict_Rest)

def create_review(request):
    review=Review.objects.all()
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save() 
    form = ReviewForm()
    dict_Rvw = {
        'form': form,
        'review':review         
    }
    return render(request, 'create_review.html', dict_Rvw)

#creating viewset for Restaurant and Review models

class RestaurantViewSet(viewsets.ModelViewSet):
    queryset= Restaurant.objects.all()
    serializer_class= RestaurantSerializer
    
class ReviewViewSet(viewsets.ModelViewSet):
    queryset= Review.objects.all()
    serializer_class= ReviewSerializer
    

    


