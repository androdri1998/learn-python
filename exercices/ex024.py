city = str(input("Type a city name: ")).strip()

city_splited = city.split()
first_name_city_upper_letters = city_splited[0].upper()
if first_name_city_upper_letters == "SANTO":
    print("City name starts with 'SANTO'")
else:
    print("City name doesn't start with 'SANTO'")
