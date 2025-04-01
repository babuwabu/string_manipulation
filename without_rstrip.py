# ask user for input
user = input("Enter your name: ")
# manually remove trailing spaces 
while len(user) > 0 and user[-1] == " ":
    user = user[:-1]
# print output
print(repr(user))
