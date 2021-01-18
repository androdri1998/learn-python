fullname = input("Type your full name: ")

fullname_upper = fullname.upper()
fullname_lower = fullname.lower()

fullname_splited = fullname.split()
amount_characters_first_name = len(fullname_splited[0])

amount_characters_full_name = 0
for name in fullname_splited:
    amount_characters_full_name += len(name)

print("Full name with upper letters: {}".format(fullname_upper))
print("Full name with lower letters: {}".format(fullname_lower))
print("Amount characters at full name: {} characters".format(amount_characters_full_name))
print("Amount characters at first name: {} characters".format(amount_characters_first_name))
