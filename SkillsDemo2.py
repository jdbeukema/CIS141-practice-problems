# Get the user's name as input and save to variable (username)
username = input("What is your name? ")
print("")
print("Hello",username)

# Get the number of people as input and save to variable (num_of_people)
num_of_people = int(input("How many people are in your party? "))
print("")

# Get total bill as input and save to variable (total_bill)
total_bill = float(input("What is the total bill? $"))
print("")

# Do the math and save result to new variable (split)
split = (total_bill/num_of_people)

# Print a friendly message that incorporates both the split and username variables
print(f"{username}, please ask each person pay ${split:.2f}.")



