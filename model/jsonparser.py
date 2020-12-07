import json
import urllib2

f = open('googleresponse.json')

data = json.load(f);

def get_names_from_json(json):
    names_list = []
    try:
        for i in range(0, 5):
            json_results = json["results"]
            name = json_results[i]["name"]
            names_list.append(name)
    except IndexError:
            return names_list

    return names_list

def get_store_status(json):
    statuses = []
    try:
        for i in range(0, 5):
            json_results = json["results"]
            status= json_results[i]["opening_hours"]["open_now"]
            statuses.append(status)
    except IndexError:
            return statuses
    return statuses

def get_ratings_from_json(json):
    ratings_list = []
    try:
        for i in range(0, 5):
            json_results = json["results"]
            rating = json_results[i]["rating"]
            ratings_list.append(rating)
    except IndexError:
            return ratings_list

    return ratings_list

def get_addresses_from_json(json):
    address_list = []
    try:
        for i in range(0, 5):
            json_results = json["results"]
            address = json_results[i]["vicinity"]
            address_list.append(address)
    except IndexError:
            return address_list

    return address_list



def get_icon_from_json(json):
    try:
            json_results = json["results"]
            icon = json_results[i]["icon"]
	img = urllib2.urlopen(icon).read()

    return  img


def get_place_id_from_json(json):
    place_id_list = []
    try:
        for i in range(0, 5):
            json_results = json["results"]
            place_id = json_results[i]["place_id"]
            place_id_list.append(place_id)
    except IndexError:
            return place_id_list

    return place_id_list


f.close();