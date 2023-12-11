import json

def map_value(value, mapping):
    for dest_start, src_start, length in mapping:
        if src_start <= value < src_start + length:
            return dest_start + (value - src_start)
    return value

def process_almanac(seeds, mappings):
    results = []
    for seed in seeds:
        current_value = seed
        for mapping in mappings:
            current_value = map_value(current_value, mapping)
        results.append(current_value)
    return min(results)

# Load data from JSON file
with open('almanac_data.json', 'r') as file:
    data = json.load(file)

seeds = data['seeds']
mappings = [
    data['seed_to_soil_map'],
    data['soil_to_fertilizer_map'],
    data['fertilizer_to_water_map'],
    data['water_to_light_map'],
    data['light_to_temperature_map'],
    data['temperature_to_humidity_map'],
    data['humidity_to_location_map']
]

# Process the almanac
lowest_location = process_almanac(seeds, mappings)
print(f"The lowest location number is {lowest_location}")
