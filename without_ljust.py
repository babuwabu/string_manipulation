# ask user for input
user = input("Enter your name: ")
width = int(input("Enter the total width: "))

# add spaces to the end of the name to match the specified width
if len(user) < width:
    user += " " * (width - len(user))

# print output
print(user, "'")