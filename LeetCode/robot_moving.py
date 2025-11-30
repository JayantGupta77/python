class Robot:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def move(self, direction, steps):
        if direction == 'u':   
            self.y += steps
        elif direction == 'd':   
            self.y -= steps
        elif direction == 'l':  
            self.x -= steps
        elif direction == 'r':   
            self.x += steps

    def get_position(self):
        return (self.x, self.y)

robot = Robot()
while True:
    cmd = input("Enter command (u/d/l/r + steps, e.g. u5, r3). Press Enter to exit: ")
    if not cmd:
        break
    direction = cmd[0]
    steps = int(cmd[1:])
    robot.move(direction, steps)
    print("Robot position:", robot.get_position())
