# ask user for input
user = input("Enter ypur name: ")
prefix = input("Enter the prefix to check: ")
# manually check if the string starts with the given prefix 
starts_with = len(user) >= len(prefix) and user[:len(prefix)] == prefix
# print the output
print(starts_with)