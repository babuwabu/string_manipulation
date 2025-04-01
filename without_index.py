# ask user for input
user = input("Enter your name: ")
char_find = input("Enter the character to find: ")
# find the first occurrence manually
index = -1
for i in range(len(user)):
    if user[i] == char_find:
        index = i
        break
# print the output
if index != -1:
    print(f"The character '{char_find}' first appears at index {index}.")
else:
    print(f"The character '{char_find}' is not found in the string.")
