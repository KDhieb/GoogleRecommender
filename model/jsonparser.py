import json
import base64

from datetime import date
import datetime

class jsonparser:
    data = None
    names_list = []
    ratings_list = []
    address_list = []
    place_id_list = []

    def getData(self, location_list):
        names_list = []
        ratings_list = []
        address_list = []
        busyness_list = []
        for i in range (0, len(location_list)):
             today = datetime.datetime.today().weekday()
             hour = datetime.datetime.now().hour
             if 'populartimes' in location_list[i].keys():
                 busyness_list.append(location_list[i]["populartimes"][today]["data"][hour]);
             else:
                 break;
             name = location_list[i]["name"];
             names_list.append(name);
             ratings_list.append(location_list[i]["rating"]);
             address_list.append(location_list[i]["address"])


        print("Names of Locations: ")
        print("\n")
        print(names_list);
        print("ratings list: ")
        print("\n")
        print(ratings_list);
        print("Address list: ")
        print("\n")
        print(address_list);
        print("Busyness ratings: ")
        print("\n")
        print(busyness_list);



    def openFile(self, filename):
        f = open(filename)
        data = json.load(f)

    def get_names_from_json(self, json):
        try:
            for i in range(0, 5):
                json_results = json["results"]
                name = json_results[i]["name"]
                self.names_list.append(name)
        except IndexError:
                return self.names_list
        return self.names_list

    def get_store_status(self, json):
        try:
            for i in range(0, 5):
                json_results = json["results"]
                status= json_results[i]["opening_hours"]["open_now"]
                self.statuses.append(status)
        except IndexError:
                return self.statuses
        return self.statuses

    def get_ratings_from_json(self, json):
        try:
            for i in range(0, 5):
                json_results = json["results"]
                rating = json_results[i]["rating"]
                self.ratings_list.append(rating)
        except IndexError:
                return self.ratings_list

        return self.ratings_list

    def get_addresses_from_json(self, json):
        try:
            for i in range(0, 5):
                json_results = json["results"]
                address = json_results[i]["vicinity"]
                self.address_list.append(address)
        except IndexError:
                return self.address_list

        return self.address_list

    @staticmethod
    def get_icon_from_json(json):
        global icon
        try:
            json_results = json["results"]
            icon = json_results[0]["icon"]
        except:
            ...
        img = base64.urlsafe_b64decode(icon)
        return  img

    def get_place_id_from_json(self, json):
        try:
            for i in range(0, 5):
                json_results = json["results"]
                place_id = json_results[i]["place_id"]
                self.place_id_list.append(place_id)
        except IndexError:
                return self.place_id_list
        return self.place_id_list


