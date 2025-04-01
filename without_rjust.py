# ask user for input
user = input("Enter your name: ")
width = int(input("Enter the total width: "))
# add spaces to the beginning of the name to match the specified width
if len(user) < width:
    user = " " * (width - len(user)) + user
# print the output
print(repr(user))