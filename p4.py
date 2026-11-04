import time

"""
CSE 465 - Project #4

GROUP MEMBERS AND RESPONSIBILITIES (fill in names before submission):
    Person 1: [NAME] - CommonCityNames.txt
        Read states.txt and zipcode data; find unique city names present
        in EVERY listed state; sort names and output one per line.
        Bonus responsibility: use filter() where it makes sense.

    Person 2: [NAME] - LatLon.txt + integration/testing
        Read zips.txt and zipcode data; output latitude and longitude
        for each requested ZIP in input order; use the FIRST matching
        record for duplicate ZIP codes. Integrate and test all sections.
        Bonus responsibility: use yield for streaming zipcode records.

    Person 3: [NAME] - CityStates.txt
        Read cities.txt and zipcode data; find unique states for each
        requested city; sort state names and output one line per city.
        Bonus responsibility: use lambda where it makes sense.

All members: test edge cases, use comprehensions when appropriate,
avoid unnecessary repeated scans, and explain your own code.

IMPORTANT:
    - Keep the provided runtime-measurement lines in __main__.
    - Put helper functions above __main__; put function CALLS inside it.
    - Coordinate the exact format of the zipcode data before coding.
    - Update the bonus line-number comments below AFTER final edits.
    - Submit the finished file as p4.py (not p4_group_template.py).
"""

"""
BONUS FEATURE LOCATIONS - replace dots with actual line numbers:
1- => Lambda was used in line/s: ............
2- => Filter or map was used in line/s: ............
3- => yield was used in line/s: ............
"""


# =====================================================================
# SHARED HELPER AREA (PERSON 2 coordinates with Persons 1 and 3)
# =====================================================================
# Write reusable zipcode-reading helpers HERE, above the task functions.
# If implementing the yield bonus, define the generator here.
# Decide whether each task should call the generator separately or share
# a preprocessed lookup. Do not consume a generator and expect to reuse it.
# =====================================================================


# =====================================================================
# PERSON 1 - CommonCityNames.txt
# =====================================================================
# WRITE PERSON 1'S FUNCTION(S) HERE.
# Inputs: states.txt and the zipcode dataset.
# Output: CommonCityNames.txt, sorted unique city names appearing in ALL
#         requested states, one name per line.
# Bonus: filter() if it improves clarity.
# Suggested function name: generate_common_city_names()
# =====================================================================


# =====================================================================
# PERSON 2 - LatLon.txt
# =====================================================================
# WRITE PERSON 2'S FUNCTION(S) HERE.
# Inputs: zips.txt and the zipcode dataset.
# Output: LatLon.txt; one latitude/longitude pair per input ZIP, with a
#         space between values; use the first zipcode record on duplicates.
# Bonus: yield in the shared zipcode reader above.
# Suggested function name: generate_lat_lon()
# =====================================================================


# =====================================================================
# PERSON 3 - CityStates.txt
# =====================================================================
# WRITE PERSON 3'S FUNCTION(S) HERE.
# Inputs: cities.txt and the zipcode dataset.
# Output: CityStates.txt; one line per input city, with sorted, distinct
#         state names separated by spaces.
# Bonus: lambda in a useful key or transformation.
# Suggested function name: generate_city_states()
# =====================================================================


if __name__ == "__main__":
    start_time = time.perf_counter()  # Do not remove this line
    '''
    Inside the __main__, do not add any codes before this line.
    -----------------------------------------------------------
    '''

    # =================================================================
    # FINAL INTEGRATION
    # =================================================================
    # Uncomment these calls ONLY after the corresponding functions exist.
    # generate_common_city_names()  # Person 1
    # generate_lat_lon()            # Person 2
    # generate_city_states()        # Person 3
    # =================================================================

    '''
    Inside the __main__, do not add any codes after this line.
    ----------------------------------------------------------
    '''
    end_time = time.perf_counter()
    # Calculate the runtime in milliseconds
    runtime_ms = (end_time - start_time) * 1000
    print(f"The runtime of the program is {runtime_ms} milliseconds.")
