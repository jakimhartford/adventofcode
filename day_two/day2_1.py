def is_game_possible(game_data, bag_capacity):
    # Initialize maximum cubes shown for each color
    max_cubes_shown = {"red": 0, "green": 0, "blue": 0}

    # Process each pull in the game
    for pull in game_data:
        for color, count in pull:
            # Update the maximum number of cubes shown for each color
            max_cubes_shown[color] = max(max_cubes_shown[color], count)

            # Check if the count exceeds the bag's capacity
            if max_cubes_shown[color] > bag_capacity[color]:
                return False

    return True

def analyze_games(games):
    # Define the bag's capacity
    bag_capacity = {"red": 12, "green": 13, "blue": 14}

    # Initialize the sum of IDs of possible games
    possible_games_sum = 0

    # Analyze each game
    for game_id, game_data in games.items():
        if is_game_possible(game_data, bag_capacity):
            possible_games_sum += game_id

    return possible_games_sum


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

def analyze_games_from_file(file_path):
    games = {}
    with open(file_path, 'r') as file:
        for line in file:
            game_id, game_data = parse_game_data(line.strip())
            games[game_id] = game_data

    return analyze_games(games)

# Example usage
file_path = 'games.txt'  # Replace with your file path
sum_of_possible_games = analyze_games_from_file(file_path)
print("Sum of IDs of possible games:", sum_of_possible_games)
