# ask user for input
user = input("Enter your name: ")
width = int(input("Enter the total width: "))
# add zeros to the beginning of the string to match the specified width
if len(user) < width:
    user = "0" * (width - len(user)) + user
# print the output
print(repr(user))