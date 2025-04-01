# ask user for input
user = input("Enter your name: ")
# manually check if all characters are lowercase 
is_lower = True

for char in user:
    if "A" <= char <= "Z": 
        is_lower = False
        break
# print the output
print(is_lower)