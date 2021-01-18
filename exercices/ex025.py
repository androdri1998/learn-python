fullname = input("Type a full name: ")

fullname_upper_letters = fullname.upper()
if fullname_upper_letters.find("SILVA") >= 0:
    print("Full name contain name 'SILVA'")
else:
    print("Full name doesn't contain name 'SILVA'")
