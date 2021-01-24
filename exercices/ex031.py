try:
    distance = int(input("How far out are we going? "))

    value_ticket = 0
    value_per_km_larger_200_km = 0.45
    value_per_km_less_200_km = 0.50

    if(distance > 200):
        value_ticket = distance * value_per_km_larger_200_km
    else:
        value_ticket = distance * value_per_km_less_200_km
    
    print('Tiket price is R$ {:.2f}'.format(value_ticket))
    
except ValueError:
    print("Value isn't a number")