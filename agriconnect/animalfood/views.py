from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def animalFoods(request):
    animalFoods = AnimalFood.objects.all()
    serializer = AnimalFoodSerializer(animalFoods,many=True)
    return Response(serializer.data)

@api_view(["GET"])
def animalFood(request,pk):
    animalFood = AnimalFood.objects.get(pk=pk)
    serializer = AnimalFoodSerializer(animalFood,many=False)
    return Response(serializer.data)

@api_view(["POST"])
def createAnimalFood(request):
    data = request.data
    animalFood = AnimalFood.create(
        name = data['name'],
        brand = data['brand'],
        description = data['description'],
        category = data['category'],
        price = data['price'],
        image = data['image'],
        quantity = data['quantity'],
        provider = data['provider']

    )
    serializer = AnimalFoodSerializer(animalFood)
    
    return Response(serializer.data)

