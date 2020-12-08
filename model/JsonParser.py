import json
import base64
import datetime
from model.Business import Business

class JsonParser:
    data = None
    names_list = []
    ratings_list = []
    address_list = []
    statuses = []
    img_list = []

    def __init__(self):
        self.business_list = []
        self.place_id_list = []
        max_listings = 5
        

    def get_filtered_business_list(self, location_list, user_latitude, user_longitude):

        for i in range(0, len(location_list)):
            if 'populartimes' in location_list[i].keys():
                today = datetime.datetime.today().weekday()
                hour = datetime.datetime.now().hour
                busyness = location_list[i]["populartimes"][today]["data"][hour]
            else:
                busyness = None
            name = location_list[i]["name"]
            address = location_list[i]["address"]
            number = location_list[i]['international_phone_number']
            rating = location_list[i]["rating"]
            business = Business(name, address, number, rating, busyness)
            business.calculate_distance_from_user(user_latitude, user_longitude)
            self.business_list.append(business)

            self.print_business_info_test(business, i)

        return self.sort_business_by_ranking(self.business_list)

    def print_business_info_test(self, business, i):
        print(f"\nBusiness {i + 1}")
        print(f"Name: {business.name}")
        print(f"Address: {business.address}")
        print(f"Number: {business.number}")
        print(f"Rating: {business.rating}")
        print(f"Busyness: {business.busyness}")
        print(f"Distance: {business.distance}")
        print("\n")

    def get_place_id_from_json(self, json, max_listings):
        try:
            num_of_results = 0
            pos = 0
            while num_of_results < max_listings:
                json_results = json["results"]
                try:
                    status = json_results[pos]["opening_hours"]["open_now"]
                    if status == True:
                        place_id = json_results[pos]["place_id"]
                        self.place_id_list.append(place_id)
                        pos += 1
                        num_of_results += 1
                    else:
                        pos += 1
                except (IndexError, KeyError):
                    place_id = json_results[pos]["place_id"]
                    self.place_id_list.append(place_id)
                    pos += 1
                    num_of_results += 1
                else:
                    pos += 1
        except IndexError:
                return self.place_id_list
        return self.place_id_list

    def sort_business_by_ranking(self, biz_list):
        try:
            self.sorted_business_list = sorted(biz_list, key=lambda x: x.busyness)
            if not self.sorted_business_list:
                 self.sorted_business_list = sorted(biz_list, key=lambda x: x.distance)
            return self.sorted_business_list
        except TypeError:
            return biz_list






