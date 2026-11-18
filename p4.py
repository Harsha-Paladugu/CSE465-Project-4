import time

"""
CSE 465 - Project #4

Group members and responsibilities:

    Harsha Paladugu - CommonCityNames.txt
        Wrote generate_common_city_names(): reads states.txt, collects the
        city names for each of those states, and writes the names found in
        every state (sorted, no duplicates, one per line). Used filter() for
        the bonus. Also matched the shared reader to the real zipcodes.txt
        layout (tab separated, header row), put the three parts together
        in main, and tested the outputs.

    Evan Bailey - LatLon.txt and the shared zipcode reader
        Wrote read_zipcodes(), the generator all three parts use to go
        through zipcodes.txt (yield bonus), and generate_lat_lon(): reads
        zips.txt and writes the latitude and longitude of each zip code,
        using the first entry when a zip code shows up more than once.

    My'Annia Lewis - CityStates.txt
        Wrote generate_city_states(): reads cities.txt and writes, for each
        city, the states that have a city with that name (sorted, each
        state listed once). Used lambda for the bonus.
"""

"""
1- => Lambda was used in line/s: 59, 105
2- => Filter or map was used in line/s: 59
3- => yield was used in line/s: 47
"""


ZIP_FILE = "zipcodes.txt"


# Goes through zipcodes.txt one record at a time instead of loading the
# whole file. Each record is a list of the tab separated columns:
# 1 = zip code, 3 = city, 4 = state, 6 = latitude, 7 = longitude
def read_zipcodes():
    with open(ZIP_FILE) as f:
        next(f, None)  # first line is the column names
        for line in f:
            parts = line.rstrip("\n").split("\t")
            if len(parts) >= 8:
                yield parts


# CommonCityNames.txt: city names that show up in every state in states.txt
def generate_common_city_names():
    with open("states.txt") as f:
        states = {line.strip().upper() for line in f if line.strip()}

    # each state gets its own set of city names
    cities_by_state = {state: set() for state in states}

    # only look at records from the states we were asked about
    for parts in filter(lambda p: p[4] in states, read_zipcodes()):
        cities_by_state[parts[4]].add(parts[3])

    # a city only counts if every state has it
    common = set.intersection(*cities_by_state.values()) if states else set()

    with open("CommonCityNames.txt", "w") as out:
        out.writelines([city + "\n" for city in sorted(common)])


# LatLon.txt: latitude and longitude for each zip code in zips.txt
def generate_lat_lon():
    with open("zips.txt") as f:
        zips = [line.strip() for line in f]

    # keep only the first entry we see for each zip code
    lookup = {}
    for parts in read_zipcodes():
        if parts[1] not in lookup:
            lookup[parts[1]] = parts[6] + " " + parts[7]

    with open("LatLon.txt", "w") as out:
        for z in zips:
            out.write(lookup.get(z, "") + "\n")


# CityStates.txt: the states that contain each city in cities.txt
def generate_city_states():
    with open("cities.txt", "r") as file:
        cities = [line.strip() for line in file if line.strip()]

    # lowercase the names so "Oxford" matches "OXFORD" in the data
    city_states = {city.lower(): set() for city in cities}

    for record in read_zipcodes():
        city = record[3].strip().lower()
        state = record[4].strip()

        if city in city_states:
            city_states[city].add(state)

    with open("CityStates.txt", "w") as output_file:
        for city in cities:
            # states in alphabetical order
            states = sorted(
                city_states[city.lower()],
                key=lambda state: state.lower()
            )
            output_file.write(" ".join(states) + "\n")


if __name__ == "__main__":
    start_time = time.perf_counter()  # Do not remove this line
    '''
    Inside the __main__, do not add any codes before this line.
    -----------------------------------------------------------
    '''

    generate_common_city_names()
    generate_lat_lon()
    generate_city_states()

    '''
    Inside the __main__, do not add any codes after this line.
    ----------------------------------------------------------
    '''
    end_time = time.perf_counter()
    # Calculate the runtime in milliseconds
    runtime_ms = (end_time - start_time) * 1000
    print(f"The runtime of the program is {runtime_ms} milliseconds.")
