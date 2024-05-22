# Import necessary modules
from app.modelsfeed_amenity_types import AmenityType

# Define the list of unique amenity types
amenity_types = [
    {"name": "Doctor on Call"},
    {"name": "Dry Cleaning"},
    {"name": "Laundry Service Available"},
    {"name": "Lobby"},
    {"name": "Parking Facilities Available"},
    {"name": "Airport Transfer Available / Surcharge"},
    {"name": "Banquet Facilities"},
    {"name": "Business Center"},
    {"name": "Currency Exchange"},
    {"name": "Swimming Pool"},
    {"name": "Bar / Lounge"},
    {"name": "Multi Cuisine Restaurant"},
    {"name": "Free Parking"},
    {"name": "Local Tour / Travel Desk"},
    {"name": "Fine Dining Restaurant"},
    {"name": "Fitness Center"},
    {"name": "24-hour Front Desk"},
    {"name": "Spa"},
    {"name": "Infinity Pool"},
    {"name": "Butler Service"},
    {"name": "Luxury Spa"},
    {"name": "Butler Service"},
    {"name": "Boat Ride"},
    {"name": "Luxury Restaurant"},
    {"name": "Outdoor Pool"},
    {"name": "Multiple Restaurants"},
    {"name": "Free Airport Shuttle"},
    {"name": "Free Wi-Fi"},
    {"name": "Outdoor Pool"}
]

# Iterate through the list and create or get AmenityType objects
for amenity_data in amenity_types:
    amenity_name = amenity_data["name"]
    # Check if amenity type already exists
    existing_amenity = AmenityType.objects.filter(name=amenity_name).first()
    if not existing_amenity:
        # Amenity type doesn't exist, create a new one
        AmenityType.objects.create(name=amenity_name)
    else:
        # Amenity type already exists, do nothing
        pass
