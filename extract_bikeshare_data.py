# extract_bikeshare_data.py

import code # to debug: `code.interact(local=locals())`
import os
from pprint import pprint
import pybikes
import json
import csv

networks_dot_csv = os.path.join(os.path.dirname(__file__), "data/networks.csv")
print "WRITING TO CSV FILE -- %(file_name)s" % {"file_name": networks_dot_csv}
#os.remove(networks_dot_csv) if os.path.isfile(networks_dot_csv) else "NO CSV FILE DETECTED"
#networks_csv = csv.writer(open(networks_dot_csv, "w"))
#networks_csv.writerow(["id","tag","name","url","city","lat","lng","radius"])

bikeshares_dot_csv = os.path.join(os.path.dirname(__file__), "data/bikeshares.csv")
print "WRITING TO CSV FILE -- %(file_name)s" % {"file_name": bikeshares_dot_csv}
os.remove(bikeshares_dot_csv) if os.path.isfile(bikeshares_dot_csv) else "NO CSV FILE DETECTED"
bikeshares_csv = csv.writer(open(bikeshares_dot_csv, "w"))
bikeshares_csv.writerow(["city","company","country","latitude","longitude","name","tag"])


networks_dot_json = os.path.join(os.path.dirname(__file__), "fixtures/citybikes_api/get_networks.json")
with open(networks_dot_json) as json_file:
    networks = json.load(json_file)
    for network in networks:

        network_tag = network["tag"].encode()

        try:
          city_name = network["city"].encode()
        except UnicodeEncodeError:
          city_name = "#UNENCODABLE"

        n = {
          'id': network["id"],
          #'tag': network_tag, tag is the same as name
          'name': network["name"].encode(),
          #'url': network["url"].encode(),
          #'city': city_name,
          #'lat': network["lat"],
          #'lng': network["lng"],
          'radius': network["radius"]
        }
        pprint(n)
        #networks_csv.writerow([ # n.values()
        #   n["id"], n["tag"], n["name"], n["url"], n["city"], n["lat"], n["lng"], n["radius"]
        #])

        #
        # CALL API FOR GIVEN NETWORK TAG
        #

        response = pybikes.get(network_tag)

        try:
          city = response.meta["city"].encode()
        except UnicodeEncodeError:
          city = "#UNENCODABLE"

        bikeshare = {
           'tag': response.tag.encode(),
           #'feed_url': response.feed_url,
           #'feed_method': response.method.encode(),
           'city': city,
           'name': response.meta["name"].encode(),
           'country': response.meta["country"].encode(),
           'company': response.meta["company"], # list_of_encoded_strings(response.meta["company"]),
           #'system': response.meta["system"],
           'longitude': response.meta["longitude"],
           'latitude':response.meta["latitude"]
        }

        response.update()

        bikeshare["station_count"] = len(response.stations)

        pprint(bikeshare)

        for station in response.stations:
            print station.to_json()
            print "----------------------"




'''
response = pybikes.get('capital-bikeshare')

def list_of_encoded_strings(array_of_unicode_strings):
    new_list = []
    for str in array_of_unicode_strings:
        new_list.append(str.encode())
    return new_list

bikeshare = {
   'tag': response.tag.encode(),
   'feed_url': response.feed_url.encode(),
   'feed_method': response.method.encode(),
   'city': response.meta["city"].encode(),
   'name': response.meta["name"].encode(),
   'country': response.meta["country"].encode(),
   'companies': list_of_encoded_strings(response.meta["company"]),
   'system': response.meta["system"].encode(),
   'longitude': response.meta["longitude"],
   'latitude':response.meta["latitude"]
}
print bikeshare

#
# REQUEST AND PRINT INFO ABOUT EACH STATION
#

print "----------------------"
print "GETTING BIKE STATIONS..."
print "----------------------"

response.update()

for station in response.stations:
    print station.to_json()
    print "----------------------"
'''
