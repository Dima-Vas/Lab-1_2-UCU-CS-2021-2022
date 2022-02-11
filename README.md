# Lab-1_2-UCU-CS-2021-2022
Working with geopy and folium modules.

# geopy
geopy is Python language module which can help with defining the coordinates of any place round the world.

# folium
folium is Python language module which bulids a world map and marks it depending on your customization.

# Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install geopy and folium.

```bash
pip install geopy
pip install folium

# Usage
returns (49.83826,24.02324)
>>> from  geopy.geocoders import Nominatim
>>> geolocator = Nominatim(user_agent="MyApp")
>>> loc = geolocator.geocode("Ukrainian Catholic University, L'viv Oblast, L'viv, Ukraine")

To use folium, familiarize yourself with this link : https://python-visualization.github.io/folium/modules.html#module-folium.map

# Contributing
Contribution is not allowed. Simply for grading.

## License
[MEAT](https://dontchoosealicense.com/licenses/meat/)
