def growing_plant(up_speed, down_speed, desired_height):
    
    day = 0
    if not ( 5 <= up_speed <= 100 ):
        return day + 1
    # 2 ≤ downSpeed < upSpeed.    
    if not ( 2 <= down_speed < up_speed ):
        return day + 1
    # 4 ≤ desiredHeight ≤ 1000    
    if not (4 <= desired_height <= 1000):
        return day + 1
     
    while desired_height > 0:
        desired_height = desired_height - up_speed
        day += 1
        if desired_height > 0:
            desired_height = desired_height + down_speed
    return day
    
