try:
    speed = int(input("how fast is the car? KM "))
    
    
    traffic_ticket = 0
    traffic_ticket_per_km = 7
    max_speed = 80

    if(speed > max_speed):
        difference_speed = speed - max_speed
        traffic_ticket = difference_speed * traffic_ticket_per_km
    
    print('you were fined R$ {:.2f}'.format(traffic_ticket) if traffic_ticket > 0 else 'you were not fined')
    
except ValueError:
    print("Value isn't a number")