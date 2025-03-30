# ask user for input
user = input("Enter your name: ")
# check if all characters are uppercase
all_upper = True

for char in user:
    if "a" <= char <= "z":  # checks if there are any lowercase letter found
        all_upper = False
        break
# print the result
print(all_upper)
