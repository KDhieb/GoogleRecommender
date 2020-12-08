from geopy.geocoders import Nominatim
from geopy.distance import geodesic

class Business:

    def __init__(self, name, address, number, rating, busyness=None):
        self.name = name
        self.address = address
        self.number = number
        self.rating = rating
        self.busyness = busyness
        self.distance = "N/A"


    def calculate_distance_from_user(self, user_latitude, user_longitude):
        try:
            geolocator = Nominatim(user_agent="business-recommender")
            location = geolocator.geocode(self.address)
            biz_latitude = location.latitude
            biz_longitude = location.longitude

            biz_coordinates = (biz_latitude, biz_longitude)
            user_coordinates = (user_latitude, user_longitude)

            distance_obj = geodesic(biz_coordinates,user_coordinates).kilometers
            removed_km = str(distance_obj)[0:-3]
            self.distance = round(float(removed_km),2)
        except Exception:
            self.distance = "N/A"









