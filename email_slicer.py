# # Method 1
# email = input("Please enter an email\n")
#
# account = email.split("@")
# details = {
#     "username": account[0],
#     "domain": account[1]
#            }
#
# for key in details:
#     print(key + ":" + details[key])


# Method 2

email = input("Please enter an email\n")

account = email.strip()
index = email.index("@")          # Getting the index of "@"
details = {
    "username": account[:index],  # slicing from the beginning to the index of "@"
    "domain": account[index+1:]   # slicing from character after @ till the end
           }

for key in details:
    print(key + ":" + details[key])
