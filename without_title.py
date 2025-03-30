# ask user for input
user = input("Enter your name: ")
# manually convert to title case 
title = " ".join(word[0].upper() + word[1:].lower() if word else "" for word in user.split())
# print output
print(title)