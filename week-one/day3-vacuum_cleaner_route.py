# This question is asked by Amazon. Given a string representing the sequence of moves a robot vacuum makes, return whether or not it will return to its original position. The string will only contain L, R, U, and D characters, representing left, right, up, and down respectively.

def check_initial_position(moves):
    x = 0
    y = 0
    split_moves = list(moves)
    for move in split_moves:
        if move == "L":
            x -= 1
        elif move == "R":
            x += 1
        elif move == "D":
            y -= 1
        elif move == "U":
            y += 1

    if x == 0 and y == 0:
        return True
    else:
        return False


print(check_initial_position("LR"))
print(check_initial_position("URURD"))
print(check_initial_position("RUULLDRD"))