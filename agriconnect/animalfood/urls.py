from django.urls import path
from .views import *
urlpatterns = [
    path('animalfoods/',animalFoods,name='animalfood'),
    path('animalfood/<int:pk>',animalFood,name='animalfood'),
    path('createanimalfood/',createAnimalFood,name='createAnimalFood')
]
