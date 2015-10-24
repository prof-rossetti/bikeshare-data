# extract_bikeshare_data.py

import code # to debug: `code.interact(local=locals())`
import pybikes
import json

print("GETTING BIKE DATA...")

response = pybikes.get('capital-bikeshare')

agency = response.meta
feed_url = response.feed_url
feed_type = response.method

response.update()




print("WRITING DATA TO FILE")
