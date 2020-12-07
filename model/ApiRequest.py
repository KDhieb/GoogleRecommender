import requests
import geocoder
import populartimes

from model.jsonparser import jsonparser

g = geocoder.ip('me')
print(g.latlng)


class ApiRequest:
    api_key = ""
    jsonparser = None
    latitude = None
    longitude = None

    def __init__(self):
        file = open("apikey.txt", 'r')
        key = file.read()
        self.api_key = key
        self.jsonparser = jsonparser()
        self.get_geolocation()


    def get_geolocation(self):
        g = geocoder.ip('me')
        geoArray = g.latlng
        self.latitude = geoArray[0]
        self.longitude = geoArray[1]


    def initial_query(self, radius, keyword):
        url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={self.latitude}, {self.longitude}&radius={radius}&keyword={keyword}&key={self.api_key}"

        print(url)
        r = requests.get(url)
        response_dict = r.json()

        return response_dict

    def get_place_information(self):
        radius = input("Enter Radius: ")
        keyword = input("Enter Keyword: ")
        ids_list = jsonparser.get_place_id_from_json(self.jsonparser, self.initial_query(radius, keyword))
        information_list = []
        for id in ids_list:
            information_list.append(populartimes.get_id(self.api_key, id))
        print(information_list)
        return information_list

    def parse_place_information(self):
        ...




if __name__ == '__main__':
    apr = ApiRequest()
    apr.get_place_information()


