#!/usr/bin/env python 
# -*- coding: utf-8 -*-

import keys, names, urllib.request, json, time

REQUESTS_PER_MINUTE = 30
SLEEP_TIME = (60/REQUESTS_PER_MINUTE)+0.5 # 30 requests per second limit


URL_location = "http://api.sl.se/api2/typeahead.json?maxresults=50&key=" + keys.sl_location_key + "&searchstring="
result = dict()

print("-- START --")

# Search for every character (a-z)
for c in range(97,123):
    print("Fetching results for: '" + chr(c) + "'")
    response = urllib.request.urlopen(URL_location + chr(c))
    content = response.read()
    data = json.loads(content.decode("utf8"))

    stations = data["ResponseData"]
    for station in stations:
        result[station["SiteId"]] = {
                                     "name"     : station["Name"],
                                     "siteID"   : station["SiteId"],
                                     "type"     : station["Type"],
                                     "x"        : station["X"],
                                     "y"        : station["Y"]}
    time.sleep(SLEEP_TIME)


# Dump DB to file
f = open(names.stations, 'w')
f.write(json.dumps(result))
f.close()

print(str(len(result)) + " stations fetched.")
print("-- DONE --")
