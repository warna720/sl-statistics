#!/usr/bin/env python 
# -*- coding: utf-8 -*-

import keys, names, urllib.request, json, time

# Bussar, tunnelbana, pendeltåg, spårvagn/lokalbana, båtar
buses, metros, trains, trams, ships = dict(), dict(), dict(), dict(), dict()


REQUESTS_PER_MINUTE = 60
SLEEP_TIME = (60/REQUESTS_PER_MINUTE)+0.5 # 60 requests per second limit

f = open(names.stations, 'r')
stations = json.loads(f.read())

URL_RTL = "http://api.sl.se/api2/realtimedepartures.json?timewindow=60&key=" + keys.sl_RTL_key + "&siteid="

print("-- START --")

for station in stations.values():
    print("Fetching results for: '" + station["name"] + "' : " + station["siteID"])
    response = urllib.request.urlopen(URL_RTL + station["siteID"])
    content = response.read()
    data = json.loads(content.decode("utf8"))

    schedule = data["ResponseData"]    
    if schedule["Buses"]:
        buses[station["siteID"]] = station
            
    if schedule["Metros"]:
        metros[station["siteID"]] = station
            
    if schedule["Trains"]:
        trains[station["siteID"]] = station
            
    if schedule["Trams"]:
        trams[station["siteID"]] = station
            
    if schedule["Ships"]:
        ships[station["siteID"]] = station
            
    time.sleep(SLEEP_TIME)
f.close()

result = dict()
result["buses"] = buses
result["metros"] = metros
result["trains"] = trains
result["trams"] = trams
result["ships"] = ships

# Dump results to file
f = open(names.all_transports, 'w')
f.write(json.dumps(result))
f.close()

# Also dump all transport types to their own fie
for file_name, transport_type in zip(names.get_all_types(), [buses, metros, trains, trams, ships]):
    f = open(file_name, 'w')
    f.write(json.dumps(transport_type))
    f.close()

print("-- DONE --")

