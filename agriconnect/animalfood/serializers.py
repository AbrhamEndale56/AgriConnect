from .models import *
from rest_framework.serializers import ModelSerializer
class AnimalFoodSerializer(ModelSerializer):
     class Meta:
        model: AnimalFood
        fields ="__all__"
    
class FarmerSerializer(ModelSerializer):
     class Meta:
        model: Farmer
        fields ="__all__"
class AnimalFoodProviderSerializer(ModelSerializer):
     class Meta:
        model: AnimalFoodProvider
        fields ="__all__"
class DeliverDriverSerializer(ModelSerializer):
     class Meta:
        model: DeliveryDriver
        fields ="__all__"
class OrderSerializer(ModelSerializer):
     class Meta:
        model: Order
        fields ="__all__"
class AdminstratorSerializer(ModelSerializer):
     class Meta:
        model: Administrator
        fields ="__all__"
class NotificationSerializer(ModelSerializer):
     class Meta:
        model: Notification
        fields ="__all__"
    
    
