# ask user for input
user = input("Enter your name: ")
# manually capitalize the first letter 
if user:
    capitalized = user[0].upper() + user[1:].lower()
else:
    capitalized = ""

# print output
print(capitalized)