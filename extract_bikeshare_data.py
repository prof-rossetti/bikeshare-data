# extract_bikeshare_data.py

import code # to debug: `code.interact(local=locals())`
import os
from pprint import pprint
import pybikes
import json
import csv

networks_dot_csv = os.path.join(os.path.dirname(__file__), "data/networks.csv")
print "WRITING TO CSV FILE -- %(file_name)s" % {"file_name": networks_dot_csv}
os.remove(networks_dot_csv) if os.path.isfile(networks_dot_csv) else "NO CSV FILE DETECTED"
networks_csv = csv.writer(open(networks_dot_csv, "w"), lineterminator=os.linesep)
networks_csv.writerow(["id","tag"])

bikeshares_dot_csv = os.path.join(os.path.dirname(__file__), "data/bikeshares.csv")
print "WRITING TO CSV FILE -- %(file_name)s" % {"file_name": bikeshares_dot_csv}
os.remove(bikeshares_dot_csv) if os.path.isfile(bikeshares_dot_csv) else "NO CSV FILE DETECTED"
bikeshares_csv = csv.writer(open(bikeshares_dot_csv, "w"), lineterminator=os.linesep)
bikeshares_csv.writerow(["tag","name","city","country","company","longitude","latitude","feed_url","feed_format","system_type"])

stations_dot_csv = os.path.join(os.path.dirname(__file__), "data/stations.csv")
print "WRITING TO CSV FILE -- %(file_name)s" % {"file_name": stations_dot_csv}
os.remove(stations_dot_csv) if os.path.isfile(stations_dot_csv) else "NO CSV FILE DETECTED"
stations_csv = csv.writer(open(stations_dot_csv, "w"), lineterminator=os.linesep)
stations_csv.writerow(["name","latitude","longitude","bikes","free","timestamp","extra"])

'''
def list_of_encoded_strings(array_of_unicode_strings):
    new_list = []
    for str in array_of_unicode_strings:
        new_list.append(str.encode())
    return new_list
'''

#
# PARSE KNOWN NETWORKS
#

networks_dot_json = os.path.join(os.path.dirname(__file__), "fixtures/citybikes_api/get_networks.json")
with open(networks_dot_json) as json_file:
    networks = json.load(json_file)
    for network in networks:
        network_tag = network["tag"].encode()
        network_id = network["id"]
        networks_csv.writerow([network_id, network_tag])

        #
        # CALL API FOR NETWORK
        #

        try:
          response = pybikes.get(network_tag)
        except:
            continue # workaround for `Exception: System Cyclocity needs a key to work`

        try:
          city = response.meta["city"].encode()
        except UnicodeEncodeError:
          city = "#UNENCODABLE"

        try:
          name = response.meta["name"].encode()
        except UnicodeEncodeError:
          name = "#UNENCODABLE"
        except UnicodeDecodeError:
          name = "#UNDECODABLE"

        try:
          feed_url = response.feed_url
        except:
          feed_url = None # "#UNKNOWN"

        try:
          feed_format = response.method.encode()
        except:
          feed_format = None #"#UNKNOWN"

        try:
          system_type = response.meta["system"].encode()
        except:
          system_type = None #"#UNKNOWN"

        bikeshare = {
           'tag': response.tag.encode(),
           'name': name,
           'city': city,
           'country': response.meta["country"].encode(),
           'company': response.meta["company"], # list_of_encoded_strings(response.meta["company"]),
           'longitude': response.meta["longitude"],
           'latitude':response.meta["latitude"],
           'feed_url': feed_url,
           'feed_format': feed_format,
           'system_type': system_type,
        }
        pprint(bikeshare)
        bikeshares_csv.writerow([
            bikeshare["tag"],
            bikeshare["name"],
            bikeshare["city"],
            bikeshare["country"],
            bikeshare["company"],
            bikeshare["longitude"],
            bikeshare["latitude"],
            bikeshare["feed_url"],
            bikeshare["feed_format"],
            bikeshare["system_type"]
        ]) # bikeshare.values()

        #
        # CALL API FOR STATIONS
        #

        try:
          response.update()
        except:
            continue # skip problematic calls for: ["bicipalma", et al]

        for station in response.stations:
            pprint(station.to_json())
            timestamp = station.timestamp.strftime('%Y-%m-%d %H:%M:%S')

            try:
              station_name = station.name.encode()
            except:
                station_name = None

            try:
              stations_csv.writerow([
                  station_name,
                  station.latitude,
                  station.longitude,
                  station.bikes,
                  station.free,
                  timestamp,
                  station.extra
              ]) # station.values()
            except:
                code.interact(local=locals())
