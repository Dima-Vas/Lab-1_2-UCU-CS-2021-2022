"""
Lab 1_2. Working with folium and geopy.
"""

import argparse
import folium
import re
from  geopy.geocoders import Nominatim
from haversine import haversine

m=folium.Map()

def main(src, y_to_find, lat, lon):
    """
    Reads file and currates the performance of the auxillary function. Draws map.
    """
    file=open(src, "r")
    xx=file.readline()
    while xx!="==============\n":
        xx=file.readline()

    xx=file.readline()
    content_dict=dict()

    while xx!="--------------------------------------------------------------------------------\n":
        year=re.findall(r"\(([1-3][0-1, 8-9][0-9]{2})\)", xx)
        try :
            year=year[0] if type(year)==list else year
        except IndexError:
            year="????"
        if year not in content_dict :
            content_dict[year]=[]
        content_dict[year].append(list(filter(None, xx.split("\t"))))
        xx=file.readline()
    calculation(lat, lon, content_dict[y_to_find])
    m.save("map.html")
    return "Check your map bro"

def calculation(your_lat, your_lon, to_filter):
    """
    Calculates the closest points on map and adds them to the map.
    """
    folium.Marker(icon=folium.DivIcon(html="""
    <img style="width: 200%;" 
    src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/ed/Map_pin_icon.svg/1200px-Map_pin_icon.svg.png"
     alt="">
    """)
    ,location=[your_lat,your_lon], popup="You are here",).add_to(m)
    geolocator = Nominatim(user_agent="MyApp")
    i=0
    j=0
    already=dict()
    while j<len(to_filter) and i<len(to_filter) and len(list(already.keys()))<50:
        for addr in range(len(to_filter[i][1].split(","))-1):
            try:
                to_find=to_filter[i][1].split(",")[addr:-1]
                loc = geolocator.geocode(to_find)
                if (loc.latitude, loc.longitude) not in already:
                    already[(loc.latitude, loc.longitude)] = []
                already[loc.latitude, loc.longitude].append(",".join(to_find))
                j+=1
            except AttributeError :
                pass
        i+=1
    for i in range(10):
        changed_list=[haversine((x[0], x[1]), (your_lat, your_lon)) for x in already.keys()]
        id_to_find=list(already.keys())[changed_list.index(min(changed_list))]
        folium.Marker(location=[id_to_find[0],id_to_find[1]], popup=already[id_to_find][0],).add_to(m)
        del already[id_to_find]
    else :
        return []



if __name__ == "__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument('--year', type=str, required=True)
    parser.add_argument('--lat', type=str, required=True)
    parser.add_argument('--lon', type=str, required=True)
    parser.add_argument('--path', type=str, required=True)
    args = parser.parse_args()
    main(args.path, args.year, int(args.lat), int(args.lon))