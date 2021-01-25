try:
    speed = float(input("how fast is the car? KM "))
    
    traffic_ticket = 0
    traffic_ticket_per_km = 7
    max_speed = 80

    if(speed > max_speed):
        difference_speed = speed - max_speed
        traffic_ticket = difference_speed * traffic_ticket_per_km
    
    print('FINED! you were fined in R$ {:.2f}'.format(traffic_ticket) if traffic_ticket > 0 else 'Have a good day, drive with careful.')
    
except ValueError:
    print("Value isn't a number")