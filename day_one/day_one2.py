import re

def convert_text_to_digits(text):
    number_map = {
        'one': '1', 'two': '2', 'three': '3', 'four': '4', 
        'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'
    }
    for word, digit in number_map.items():
        # Using regular expressions to replace each textual number
        text = re.sub(rf'{word}', digit, text)
    return text

# Rest of the function remains the same

def sum_calibration_values_from_file(file_path):
    total_sum = 0
    with open(file_path, 'r') as file:
        for line in file:
            # Convert textual numbers to digits
            converted_line = convert_text_to_digits(line.strip())
           

            # Find all digits in the converted line
            digits = [d for d in converted_line if d.isdigit()]

    
            # If only one digit is present, concatenate it with itself
            if len(digits) == 1:
                calibration_value = int(digits[0] + digits[0])
            else:
                # Combine the first and last digit to form a two-digit number
                calibration_value = int(digits[0] + digits[-1])

            # print(line.strip())
            print(converted_line, calibration_value)
            # Add this value to the total sum
            total_sum += calibration_value
            


    return total_sum

# Example usage
file_path = 'calibration_test.txt'
print(sum_calibration_values_from_file(file_path))
