# extract_bikeshare_data.py

import pybikes # https://github.com/eskerda/PyBikes

print("GETTING BIKE DATA...")

capital_bikeshare = pybikes.get('capital-bikeshare')
print(capital_bikeshare.meta)
print(len(capital_bikeshare.stations))
capital_bikeshare.update()
print(len(capital_bikeshare.stations))
print(capital_bikeshare.stations[0])

print("WRITING DATA TO FILE")
