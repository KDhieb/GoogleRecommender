import json

f = open('googleresponse.json')

data = json.load(f);

def jsonParser(json):
    for i in range(0, 5):
        list = json["results"];
        name = list[i]["name"];
        print(name);



jsonParser(data);

f.close();