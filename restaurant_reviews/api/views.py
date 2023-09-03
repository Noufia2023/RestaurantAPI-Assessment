from rest_framework.response import Response
from rest_framework.decorators import api_view
from reviews.models import Restaurant,Review
from . serializers import RestaurantSerializer,ReviewSerializer

@api_view(['GET'])
def getData(request):
    items = Restaurant.objects.all()
    serializer = RestaurantSerializer(items, many = True)
    return Response(serializer.data)

@api_view(['GET'])
def getReviewData(request):
    items = Review.objects.all()
    serializer = ReviewSerializer(items, many = True)
    return Response(serializer.data)

@api_view(['POST']) 
def  addItem(request):
        serializer = ReviewSerializer(data =request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)


@api_view(['POST']) 
def  reviewUpdate(request,pk):
        items= Review.objects.get(id=pk)
        serializer = ReviewSerializer(instance=items, data =request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)


@api_view(['DELETE']) 
def  reviewDelete(request,pk):
        items= Review.objects.get(id=pk)
        items.delete()
        return Response('Item successfully deleted!')



            






