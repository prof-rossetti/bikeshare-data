# extract_bikeshare_data.py

import code # to debug: `code.interact(local=locals())`
import pybikes
import json


#
# REQUEST A LIST OF ALL KNOWN BIKESHARES
#

print "----------------------"
print "GETTING BIKESHARES..."
print "----------------------"

# todo

#
# REQUEST AND PRINT INFO ABOUT EACH BIKESHARE
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
