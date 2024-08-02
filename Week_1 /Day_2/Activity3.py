# A shop sells apples for 25p per apple.
# Create a program which asks a user how many apples they want to buy.
# Display the total cost of the apples in both pence, and pounds and pence.

# apple_cost = 25

# num_apples = int(input("how many apple would you like to buy?>>"))

# total_cost = num_apples * apple_cost 
# print(f" The total cost is £{total_cost / 100}")

# print(f" The total cost is {total_cost / 100} pound and {total_cost % 100}")

apple_cost = 0.25

num_apples = int(input("how many apple would you like to buy?>>"))

total_cost = num_apples * apple_cost 
print(f" The total cost is {total_cost * 100}p")

print(f" The total cost is £{total_cost:.2f}")