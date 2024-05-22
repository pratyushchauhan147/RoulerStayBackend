from django.contrib import admin
from .models import  User,Room,Property,Photo,Amenity,AmenityType,Review,PropertyType,Booking
# Register your models here.
admin.site.register(User)
admin.site.register(Room)
admin.site.register(Property)
admin.site.register(PropertyType)
admin.site.register(Photo)
admin.site.register(Amenity)
admin.site.register(AmenityType)
admin.site.register(Review)
admin.site.register(Booking)