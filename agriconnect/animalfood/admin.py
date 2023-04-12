from django.contrib import admin

from .models import *
admin.site.register(Farmer)
admin.site.register(DeliveryDriver)
admin.site.register(Order)
admin.site.register(AnimalFood)
admin.site.register(AnimalFoodProvider)
admin.site.register(Notification)
admin.site.register(Administrator)

