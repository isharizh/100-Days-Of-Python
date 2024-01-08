def right():
    turn_left()
    turn_left()
    turn_left()
def stepp():
    right()
    move()
    right()
    move()

while not at_goal():
    if wall_in_front():
        turn_left()
    else:
        move()
        while right_is_clear():
            stepp()
            if wall_in_front():
                turn_left()
                
            elif wall_on_right():
                move()