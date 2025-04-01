# ask user for input
user = input("Enter your name: ")
suffix = input("Enter the suffix to remove: ")
# manually remove the suffix
if user.endswith(suffix):
    user = user[:-len(suffix)]
# print output
print(user)