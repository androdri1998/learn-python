fullname = input("Type a full name: ")

fullname_splited = fullname.split()
first_name = fullname_splited[0]

amount_names = len(fullname_splited)
last_name = fullname_splited[amount_names - 1]

print("Fist name is '{}' and last name is '{}'".format(first_name, last_name))