def parse_game_data(line):
    # Split the line into game ID and pulls
    game_id, pulls = line.split(': ')
    game_id = int(game_id.split(' ')[1])  # Extract the numeric ID

    # Process each pull
    pulls_data = []
    for pull in pulls.split('; '):
        cubes = pull.split(', ')
        pull_data = [(c.split(' ')[1], int(c.split(' ')[0])) for c in cubes]
        pulls_data.append(pull_data)

    return game_id, pulls_data

def calculate_minimum_set_and_power(game_data):
    min_cubes = {"red": 0, "green": 0, "blue": 0}
    for pull in game_data:
        for color, count in pull:
            min_cubes[color] = max(min_cubes[color], count)
    power = min_cubes["red"] * min_cubes["green"] * min_cubes["blue"]
    return min_cubes, power

def analyze_games_from_file(file_path):
    total_power = 0
    with open(file_path, 'r') as file:
        for line in file:
            _, game_data = parse_game_data(line.strip())
            _, power = calculate_minimum_set_and_power(game_data)
            total_power += power
    return total_power

# Example usage
file_path = 'games.txt'  # Replace with your file path
total_power_sum = analyze_games_from_file(file_path)
print("Total sum of the power of the sets:", total_power_sum)
