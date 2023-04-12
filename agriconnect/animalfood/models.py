from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Permission
from django.contrib.auth.models import Group

class Farmer(AbstractUser):
    # Additional fields
    contact_number = models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    groups = models.ManyToManyField(Group, related_name='user_set_custom')
    user_permissions = models.ManyToManyField(Permission, related_name='user_permission_set_custom')

class AnimalFood(models.Model):
    name = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='animal_food/')
    quantity = models.IntegerField()
    provider = models.ForeignKey('AnimalFoodProvider', on_delete=models.CASCADE)

class Order(models.Model):
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    animal_food = models.ForeignKey(AnimalFood, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    delivery_address = models.CharField(max_length=255)
    delivery_datetime = models.DateTimeField()
    status = models.CharField(max_length=50, default='Placed')

class DeliveryDriver(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email = models.EmailField()
    contact_number = models.CharField(max_length=15)
    address = models.CharField(max_length=255)

class AnimalFoodProvider(models.Model):
    company_name = models.CharField(max_length=255)
    contact_person_name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email = models.EmailField()
    contact_number = models.CharField(max_length=15)
    address = models.CharField(max_length=255)

class Administrator(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email = models.EmailField()

class Notification(models.Model):
    driver = models.ForeignKey(DeliveryDriver, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
