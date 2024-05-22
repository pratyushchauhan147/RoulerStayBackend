# coding: utf-8
s
from app.models import AmenityType
amenity_types = [
    "Doctor on Call",
    "Dry Cleaning",
    "Laundry Service Available",
    "Lobby",
    "Parking Facilities Available",
    "Airport Transfer Available / Surcharge",
    "Banquet Facilities",
    "Business Center",
    "Currency Exchange",
    "Swimming Pool",
    "Bar / Lounge",
    "Multi Cuisine Restaurant",
    "Free Parking",
    "Local Tour / Travel Desk",
    "Fine Dining Restaurant",
    "Fitness Center",
    "24-hour Front Desk",
    "Spa",
    "Infinity Pool",
    "Butler Service",
    "Luxury Spa",
    "Butler Service",
    "Boat Ride",
    "Luxury Restaurant",
    "Outdoor Pool",
    "Multiple Restaurants",
    "Free Airport Shuttle",
    "Free Wi-Fi",
    "Outdoor Pool"
]
for amenity_name in amenity_types:
    AmenityType.objects.create(name=amenity_name)
    
get_ipython().run_line_magic('run', '')
for amenity_name in amenity_types:
    AmenityType.objects.create(name=amenity_name)
    
get_ipython().run_line_magic('save', '()')
from app.models import AmenityType
from django.db.models import Count
duplicate_names = AmenityType.objects.values('name').annotate(count=Count('name')).filter(count__gt=1)
for name in duplicate_names:
    # Get all instances of the duplicate name
    duplicates = AmenityType.objects.filter(name=name['name'])
    # Keep the first instance and delete the rest
    for duplicate in duplicates[1:]:
        duplicate.delete()
        
get_ipython().run_line_magic('save', '()')
