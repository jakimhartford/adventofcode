import json
from scipy import sparse
import numpy as np

def create_sparse_conversion_array(mapping):
    max_value = max(mapping, key=lambda x: x[0] + x[2] - 1)[0] + 1
    conversion_array = sparse.lil_matrix((max_value, 1))
    conversion_array.setdiag(np.arange(max_value))
    
    for dest_start, src_start, length in mapping:
        conversion_array[src_start:src_start + length, 0] = np.arange(dest_start, dest_start + length)
    
    return conversion_array.tocsr()

def process_seed_range(start, length, mappings):
    seeds = np.arange(start, start + length)
    
    for mapping in mappings:
        conversion_array = create_sparse_conversion_array(mapping)
        seeds = conversion_array[seeds].toarray().flatten()
    
    return seeds.min()

def process_almanac(seed_ranges, mappings):
    min_locations = []
    
    for i in range(0, len(seed_ranges), 2):
        start, length = seed_ranges[i], seed_ranges[i + 1]
        min_location = process_seed_range(start, length, mappings)
        min_locations.append(min_location)
    
    return min(min_locations)

if __name__ == "__main__":
    # Load data from JSON file
    with open('almanac_data.json', 'r') as file:
        data = json.load(file)

    seed_ranges = data['seeds']
    mappings = [data[key] for key in data.keys() if key != 'seeds']

    # Process the almanac
    lowest_location = process_almanac(seed_ranges, mappings)
    print(f"The lowest location number is {lowest_location}")

# times = [ 59,     70,     78,     78]
# distances =[430,   1218,   1213,   1276]