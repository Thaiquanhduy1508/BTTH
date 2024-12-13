def move_robot(movements):
    x, y = 0, 0
    for move in movements:
        direction, steps = move.split()
        steps = int(steps)
        if direction == "UP":
            y += steps
        elif direction == "DOWN":
            y -= steps
        elif direction == "LEFT":
            x -= steps
        elif direction == "RIGHT":
            x += steps
    return (x, y)
input_moves = [
    "UP 5",
    "DOWN 3",
    "LEFT 2",
    "RIGHT 1"
]

final_position = move_robot(input_moves)
print(f"Vị trí cuối cùng của robot là: {final_position}")
print("HÁI QUANG DUY")
