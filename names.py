stations = "stations.json"              # Unfiltered
bus_stations = "bus_stations.json"      # Bussar
metro_stations = "metro_stations.json"  # Tunnelbana
train_stations = "train_stations.json"  # Pendeltåg
tram_stations = "tram_stations.json"    # Spårvagn/lokalbana
ship_stations = "ship_stations.json"    # Båtar
all_transports = "all_transports.json"  # All transportmedel

def get_all():
    return [stations, bus_stations,
            metro_stations, train_stations,
            tram_stations, ship_stations,
            all_transports]

def get_all_types():
    return [bus_stations, metro_stations,
            train_stations, tram_stations,
            ship_stations]
