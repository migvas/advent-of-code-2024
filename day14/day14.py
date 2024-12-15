SIMULATION_TIME = 100
GRID_X = 101
GRID_Y = 103


class Robot:
    def __init__(self, pos, vel):
        self.x = int(pos[0])
        self.y = int(pos[1])
        self.vx = int(vel[0])
        self.vy = int(vel[1])

    def update_pos(self):
        self.x = self.x + self.vx
        self.x = self.x % GRID_X

        self.y = self.y + self.vy
        self.y = self.y % GRID_Y

    def time_skip(self, time):
        last_x = self.x + time * self.vx
        last_x = last_x % GRID_X

        last_y = self.y + time * self.vy
        last_y = last_y % GRID_Y

        return last_x, last_y

    def set_time_skip(self, time):
        self.x = self.x + time * self.vx
        self.x = self.x % GRID_X

        self.y = self.y + time * self.vy
        self.y = self.y % GRID_Y


input_file = "input.txt"

robots = []

quadrants = {1: 0, 2: 0, 3: 0, 4: 0}

security_level = 1

with open(input_file, "r", encoding="utf-8") as f:
    while 1:
        robot_line = f.readline().strip()

        if not robot_line:
            break

        p, v = robot_line.split(" ")

        x, y = p.split("=")[-1].split(",")
        vx, vy = v.split("=")[-1].split(",")

        robot = Robot((x, y), (vx, vy))

        robots.append(robot)

        corrected_pos = robot.time_skip(SIMULATION_TIME)

        mid_x = GRID_X // 2
        mid_y = GRID_Y // 2

        if corrected_pos[0] < mid_x:
            if corrected_pos[1] < mid_y:
                quadrants[1] += 1
            elif corrected_pos[1] > mid_y:
                quadrants[3] += 1
        elif corrected_pos[0] > mid_x:
            if corrected_pos[1] < mid_y:
                quadrants[2] += 1
            elif corrected_pos[1] > mid_y:
                quadrants[4] += 1

for q in quadrants.values():
    security_level *= q

print(f"Part 1 Solution: {security_level}")
