
colors = {
'BLACK': (0, 0, 0),
'WHITE': (255, 255, 255),
'RED': (255, 0, 0),
'LIGHTGRAY': (170, 170, 170),
'DARKGRAY': (96, 96, 96),
'BLUE': (51, 153, 215),
'GREEN': (153, 240, 51),
'TRANSPARENT': (0, 0, 0, 0),
}


class Asteroid:
    def __init__(self, x, y, direction, left_bound, right_bound, top_bound, bottom_bound, asteroid, speed):
        self.x = x
        self.y = y
        self.direction = direction
        self.left_bound = left_bound
        self.right_bound = right_bound
        self.top_bound = top_bound
        self.bottom_bound = bottom_bound
        self.asteroid = asteroid
        self.speed = speed

