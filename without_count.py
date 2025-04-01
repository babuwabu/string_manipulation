# ask user for input
user = input("Enter your name: ")
char_to_count = input("Enter the character to count: ")
# manually count the occurrences
count = 0
for char in user:
    if char == char_to_count:
        count += 1
# print the output
print(f"The character '{char_to_count}' appears {count} times in the string.")