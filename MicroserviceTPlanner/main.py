"""Microservice for travel planning software.
This program uses the geoapify api to retreive data on locations within a city
and return them into a text file.
Data returned includes:
- Location name
- Location Website, where applicable
- Location latitude and longitude
- Open hours

Usage of this sofware requires the generation of an API key for geoapify, which
can be obtained for free by following the directions on their website, and stored
in a file named "geoapify_key.txt".
"""

import requests
from requests.structures import CaseInsensitiveDict
from pprint import pprint

headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"

# Check if ready for input
with open("sites.txt", mode="r", encoding="utf-8") as sites_file:
    sites_text = sites_file.read()

site_lines = sites_text.splitlines()
# print(site_lines[0])
if site_lines[0] == "get":
    # Get search data
    area = site_lines[1]
    limit = site_lines[2]
    categories = site_lines[3]
    area_type = site_lines[4]

    # Get API key
    with open("geoapify_key.txt", mode="r", encoding="utf-8") as api_file:
        api_key = api_file.read()
    
    # Get place_id
    city_url_p1 = "https://api.geoapify.com/v1/geocode/search?text="
    city_url_p1 += area
    city_url_p2 = "&lang=en&limit=1&type="
    city_url_p2 += area_type
    city_url_p3 = "&apiKey="
    city_url_p3 += api_key

    city_url_full = city_url_p1 + city_url_p2 + city_url_p3
    # print(city_url_full) # debug

    city_resp = requests.get(city_url_full, headers=headers)
    city_response = city_resp.json()
    print(city_resp.status_code) # Debug
    if city_resp.status_code != 200:
        with open("sites.txt", mode="w", encoding="utf-8") as sites_file:
            sites_file.write("ERROR City Invalid")
    # pprint(resp.json())
    place_id = city_response["features"][0]["properties"]["place_id"]
    # pprint (city_response["features"][0]["properties"]["place_id"]) # Debug

    # Make poi url
    poi_url_p1 = "https://api.geoapify.com/v2/places?categories="
    poi_url_p1 += categories
    poi_url_p2 = "&filter=place:"
    poi_url_p2 += place_id
    poi_url_p3 = "&limit="
    poi_url_p3 += limit
    poi_url_p4 = "&apiKey="
    poi_url_p4 += api_key

    poi_url_full = poi_url_p1 + poi_url_p2 + poi_url_p3 + poi_url_p4
    # print(poi_url_full) #debug

    # Get location data
    poi_resp = requests.get(poi_url_full, headers=headers)
    print(poi_resp.status_code)
    poi_response = poi_resp.json()
    # pprint(poi_response) # Debug
    # for feature in poi_response["features"]: Debug
    #     print(feature["properties"]["name"])

    # Gather data to be returned
    lines = []
    for feature in poi_response["features"]:

        if "name" in feature["properties"]:
                line_data = feature["properties"]["name"] + ","
        else:
            line_data += "No name,"

        if "website" in feature["properties"]:
            line_data += feature["properties"]["website"] + ","
        else: 
            line_data += "No website,"

        line_data += str(feature["properties"]["lat"]) + ","
        line_data += str(feature["properties"]["lon"]) + ","

        if "opening_hours" in feature["properties"]:
            line_data += feature["properties"]["opening_hours"]
        else:
            line_data += "No hours"
        # print(line_data) # Debug
        lines.append(line_data)


    # Compile data in one string, write string to SITES_DATA
    with open("sites.txt", mode="w", encoding="utf-8") as sites_file:
        sites_file.write("got\n")

    with open("sites.txt", mode="a", encoding="utf-8") as sites_file:
        for line in lines:
            sites_file.write(line + "\n")
