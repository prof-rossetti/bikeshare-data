# extract_bikeshare_data.py

import code # to debug: `code.interact(local=locals())`
import os
from pprint import pprint

import pybikes
import json
import csv

networks_dot_json = os.path.join(os.path.dirname(__file__), "fixtures/citybikes_api/get_networks.json")
print "JSON FILE EXISTS" if os.path.isfile(networks_dot_json) else "OOPS"

networks_dot_csv = os.path.join(os.path.dirname(__file__), "data/networks.csv")
print "WRITING TO CSV FILE -- %(file_name)s" % {"file_name": networks_dot_csv}

with open(networks_dot_json) as json_file:
    networks = json.load(json_file)
    for network in networks:
        pprint(network)




























'''
#
# REQUEST AND PRINT INFO ABOUT EACH BIKESHARE "NETWORK"
#

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
