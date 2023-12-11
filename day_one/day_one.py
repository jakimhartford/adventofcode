def sum_calibration_values_from_file(file_path):
    total_sum = 0
    with open(file_path, 'r') as file:
        for line in file:
            # Find all digits in the line
            digits = [d for d in line if d.isdigit()]

            # Print the line for debugging
            print(line)

            # Check if there is at least one digit in the line
            if len(digits) >= 1:
                # If only one digit is present, concatenate it with itself
                if len(digits) == 1:
                    calibration_value = int(digits[0] + digits[0])
                else:
                    # Combine the first and last digit to form a two-digit number
                    calibration_value = int(digits[0] + digits[-1])

                # Print the digits and the calculated value for debugging
                print("First digit:", digits[0], "Last digit:", digits[-1])
                print("Calibration value:", calibration_value)

                # Add this value to the total sum
                total_sum += calibration_value

            # Break after the first line for debugging

    return total_sum

# Example usage
file_path = 'calibration_test.txt'
print(sum_calibration_values_from_file(file_path))
