def rental_car_cost(d):
    cost = d * 40
    
    if d >= 7:
        return cost - 50
    elif d >= 4:
        return cost - 20
    else:
        return cost