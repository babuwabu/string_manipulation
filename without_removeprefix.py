# ask user for name
name = input("Enter your name: ")
# define the prefix to remove
prefix_remove = input("Enter the prefix to remove: ")
# remove the prefix if it exists at the beginning of the string
if name.startswith(prefix_remove):
    name = name.replace(prefix_remove, "", 1)
# print output
print(name)
