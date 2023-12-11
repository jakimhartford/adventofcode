def is_symbol(char):
    return char in "*#$+&%-=/@."

def get_adjacent_cells(x, y, grid):
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
            yield nx, ny

def is_adjacent_to_symbol(x, y, grid):
    for nx, ny in get_adjacent_cells(x, y, grid):
        if is_symbol(grid[nx][ny]):
            return True
    return False

def extract_numbers(grid):
    numbers = []
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if grid[x][y].isdigit() and is_adjacent_to_symbol(x, y, grid):
                num = grid[x][y]
                offset = 1
                while y + offset < len(grid[0]) and grid[x][y + offset].isdigit():
                    num += grid[x][y + offset]
                    offset += 1
                numbers.append(int(num))
                # Mark the processed number with a non-digit to avoid double-counting
                for i in range(offset):
                    grid[x][y + i] = 'X'
                y += offset - 1  # Skip the rest of the number
    return numbers

def sum_part_numbers_from_file(file_path):
    with open(file_path, 'r') as file:
        grid = [list(line.strip()) for line in file]

    numbers = extract_numbers(grid)
    return sum(numbers)

# Example usage
file_path = 'part_numbers.txt'  # Replace with your file path
total_sum = sum_part_numbers_from_file(file_path)
print("Total sum of part numbers:", total_sum)
