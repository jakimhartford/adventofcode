"""
Parse the input data: You'll have a list of times allowed for each race
and the best distance ever recorded in each race.

Calculate the number of ways to beat the records for each race: 
For each race, determine how many different durations you can hold the button to beat the current record. 
This involves finding the minimum and maximum durations that would allow you to win the race.

Multiply the number of ways for each race: 
Multiply the number of ways to beat the records for all races to get 
the total number of ways you can guarantee winning all races.

Output the result: Print or return the total number of ways to win all races.
"""

def multiplyList(myList):
 
    # Multiply elements one by one
    result = 1
    for x in myList:
        result = result * x
    return result

def calculate_ways_to_beat_records(times, distances):
    ways_to_win_list = []

    for i in range(len(times)):
        time = times[i]
        distance = distances[i]
        ways_to_win = 0  # Initialize the count of ways to win

        for hold_time in range(time):
            # Initialize total_distance for this scenario
            total_distance = 0

            # Calculate the remaining travel time after holding the button
            remaining_time = times[i] - hold_time

            for t in range(remaining_time):
                total_distance += hold_time  # Calculate distance for each millisecond without button press
                # print(total_distance)

            # Check if this scenario beats the record distance
            if total_distance > distances[i]:
                ways_to_win += 1
            # Print out the scenario details
            # print(f"Hold button for {hold_time} milliseconds: {total_distance} millimeters ({'Wins' if total_distance >= distance else 'Loses'})")
        
        ways_to_win_list.append(ways_to_win)   

        # Print out the scenario details for this race
        # print(f"Race with time {time} ms and record distance {distance} mm:")
        # print(f"   Ways to win: {ways_to_win}")
        # print(f"   Total ways so far: {ways_to_win_list}")

    total_ways_to_win = multiplyList(ways_to_win_list)
    return total_ways_to_win


times = [59707878]
distances = [430121812131276]
result = calculate_ways_to_beat_records(times, distances)
print(f"Total number of ways to win all races: {result}")

# Test the function with arrays of times and distances
# times = [7, 15, 30]
# distances = [9,  40, 200]
# times = [59, 70, 78, 78]
# distances = [430, 1218, 1213, 1276]