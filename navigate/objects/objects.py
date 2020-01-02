
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


def make_spaceship (screen, x, y):
    # Ship Body
    pygame.draw.ellipse(screen, DARKGRAY, (x+5, y, 90, 60))
    pygame.draw.ellipse(screen, LIGHTGRAY, (x, y, 100, 50))

    # Red Dots
    pygame.draw.ellipse(screen, RED, (x+45, y+36, 10, 10))
    pygame.draw.ellipse(screen, RED, (x+23, y+32, 10, 10))
    pygame.draw.ellipse(screen, RED, (x+67, y+32, 10, 10))
    pygame.draw.ellipse(screen, RED, (x+7, y+20, 10, 10))
    pygame.draw.ellipse(screen, RED, (x+83, y+20, 10, 10))
    pygame.draw.ellipse(screen, RED, (x+18, y+6, 10, 10))
    pygame.draw.ellipse(screen, RED, (x+72, y+6, 10, 10))

    # Ship Cabin
    pygame.draw.ellipse(screen, BLUE, (x+20, y-10, 60, 45))

    # Alien
    pygame.draw.line(screen, GREEN, (x+45, y+32), (x+48, y+10), 5)
    pygame.draw.line(screen, GREEN, (x+55, y+32), (x+58, y+10), 5)
    pygame.draw.ellipse(screen, WHITE, (x+43, y, 10, 15))
    pygame.draw.ellipse(screen, WHITE, (x+53, y, 10, 15))
    pygame.draw.ellipse(screen, BLACK, (x+46, y+3, 5, 8))
    pygame.draw.ellipse(screen, BLACK, (x+56, y+3, 5, 8))

    # Dimensions
    # Width: 100px; Height: 60px

