# # Define a list
# colors = ["red", "green", "blue"]

# # Use a loop to access and print each color
# for i in range(len(colors)):
#     print(colors[i])

# fruits = ["apple", "banana", "cherry"]

# for index, fruit in enumerate(fruits):
#     print(f"Index {index}: {fruit}")


# fruits = ["apple", "banana", "cherry"]
# index = 0

# while index < len(fruits):
#     print(fruits[index])
#     index += 1

# fruits = ["apple", "banana", "cherry"]
# upper_fruits = [fruit.upper() for fruit in fruits]
# print(upper_fruits)  # Output: ['APPLE', 'BANANA', 'CHERRY']

# def is_long(fruit):
#     return len(fruit) > 5

# fruits = ["apple", "banana", "cherry", "blueberry"]
# long_fruits = filter(is_long, fruits)
# print(list(long_fruits))  # Output: ['banana', 'blueberry']


# names = ["Alice", "Bob", "Charlie"]
# scores = [85, 90, 95]

# for name, score in zip(names, scores):
#     print(f"{name}: {score}")

import itertools

# colors = ["red", "green", "blue"]
# for color in itertools.cycle(colors):
#     print(color)
#     # Add a break condition to avoid an infinite loop in practice
#     break
def format_first_sorted_string(strings):
    # Sort the list alphabetically
    sorted_strings = sorted(strings)
    
    # Get the first string from the sorted list
    first_string = sorted_strings[0]
    
    # Insert '***' between each letter of the string
    formatted_string = '***'.join(first_string)
    
    return formatted_string

# Example usage
strings = ["take", "over", "bitcoin", "the", "world", "maybe", "who", "knows", "perhaps"]
result = format_first_sorted_string(strings)
print(result)  # Output: b***i***t***c***o***i***n
