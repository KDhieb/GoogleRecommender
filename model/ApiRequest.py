import requests
import geocoder
import populartimes
import urllib.parse

from model.JsonParser import JsonParser

g = geocoder.ip('me')
print(g.latlng)


class ApiRequest:
    api_key = ""
    jsonparser = None
    latitude = None
    longitude = None

    def __init__(self):
        file = open("../data/apikey.txt", 'r')
        key = file.read()
        self.api_key = key
        self.jsonparser = JsonParser()
        self.get_geolocation()


    def get_geolocation(self):
        g = geocoder.ip('me')
        geoArray = g.latlng
        self.latitude = geoArray[0]
        self.longitude = geoArray[1]


    def initial_query(self, radius, keyword):
        url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?" \
              f"location={self.latitude}, {self.longitude}&" \
              f"radius={radius}&" \
              f"keyword={keyword}&" \
              f"key={self.api_key}"

        #print(url)

        r = requests.get(url)
        response_dict = r.json()

        print(response_dict)

        return response_dict

    def input_search_params(self):
        radius = input("Enter Radius: ")
        keyword = (input("Enter Keyword: "))

        return radius, keyword

    def get_place_information(self, radius, keyword):
        if not radius.isdigit():
            raise Exception
        radius_km_to_m = str(int(radius) * 1000)
        parsed_keyword = urllib.parse.quote_plus(keyword)
        ids_list = JsonParser.get_place_id_from_json(self.jsonparser, self.initial_query(radius_km_to_m, parsed_keyword))
        information_list = []
        i = 0
        for id in ids_list:
            if i < 5:
                information_list.append(populartimes.get_id(self.api_key, id))
            i+= 1
        return self.jsonparser.get_filtered_business_list(information_list, self.latitude, self.longitude)


if __name__ == '__main__':
    apr = ApiRequest()
    inputs = apr.input_search_params()
    apr.get_place_information(inputs[0], inputs[1])

