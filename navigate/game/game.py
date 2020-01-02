import pygame
from navigate.objecs.objects import *
# ================================================= INSTANCE VARIABLES ================================================*


# ===================================================== GAME SETUP ====================================================*

# PYGAME SETUP
pygame.init()
screen_width = 1250
screen_height = 800
size = (screen_width, screen_height)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Navigate")
clock = pygame.time.Clock()

# hide the mouse cursor
pygame.mouse.set_visible(False) # 0 false, 1 true

# background image
background = pygame.image.load("stars.jpg")

# MUSIC
intro_music = "pizza_theme_intro.mp3"
game_music = "gamemsc.mp3"

pygame.mixer.music.load(intro_music)
pygame.mixer.music.play(-1, 1)

# OBJECT DATA
asteroid = pygame.image.load("asteroid.png")
key = pygame.image.load("starkey.png")
navigate_title = pygame.image.load("navigate.png")
intro_background = pygame.image.load("home_background.png")

# movement speed
speed_x = 0
speed_y = 0

# spaceship starting position
current_x = 15
current_y = screen_height/2

# TEXT/FONTS
L_font = pygame.font.SysFont('Georgia', 70, True, False)
font = pygame.font.SysFont('Georgia', 60, True, False)
font2 = pygame.font.SysFont('Georgia', 30, True, False)
font3 = pygame.font.SysFont('Georgia', 15, True, False)

# ====================================================== CLASSES ======================================================*


    def move(self):
        """
        x_bound = (0, 1250)
        y_bound = (100, 800)
        direction 0 = up or decreasing y
        direction 1 = right or increasing x
        direction 2 = down or increasing y
        direction 3 = left or decreasing x

        motion:
        x increase ==> moves right
        x decrease ==> moves left
        y increase ==> moves down
        y decrease ==> moves up
        """

        if self.y <= self.top_bound:
            self.direction = 2
        elif self.y >= self.bottom_bound:
            self.direction = 0
        elif self.x <= self.left_bound:
            self.direction = 1
        elif self.x >= self.right_bound:
            self.direction = 3

        if self.direction == 0:
            self.y -= self.speed
        elif self.direction == 1:
            self.x += self.speed
        elif self.direction == 2:
            self.y += self.speed
        elif self.direction == 3:
            self.x -= self.speed
        screen.blit(self.asteroid, (self.x, self.y))

class Key:
    def __init__(self, x, y, key):
        self.x = x
        self.y = y
        self.key = key

    def place(self):
        screen.blit(self.key, (self.x, self.y))

# ====================================================== FUNCTIONS ====================================================*

def square(x):
    return x*x

# ====================================================== LEVEL SETUP ==================================================*

# variables
level = 0
deaths = 0

# LEVEL ONE CONSTRUCTION
L1_asteroids = []
for i in range(1, 6):
    L1_asteroids.append(Asteroid(i*200, screen_height/2, 2, 0, screen_width-75, 100, screen_height-64, asteroid, 15))

# LEVEL TWO CONSTRUCTION
L2_asteroids = []
for i in range(5):
    L2_asteroids.append(Asteroid(screen_width/2+150-(i*142), screen_height/2-75, 3, screen_width/2-50-(i*142), screen_width/2+150-(i*142), 100, screen_height-64, asteroid, 15))
    L2_asteroids.append(Asteroid(screen_width/2+350, screen_height-64-(i*100), 0, 0, screen_width-64, screen_height-164-(i*100), screen_height-64-(i*100), asteroid, 10))
for i in range(4):
    L2_asteroids.append(Asteroid(screen_width/2-75-(i*125), screen_height/2+75, 3, screen_width/2-200-(i*125), screen_width/2-75-(i*125), 100, screen_height-64, asteroid, 15))
for i in range(2):
    L2_asteroids.append(Asteroid(screen_width/2-75, screen_height/2+150+(i*100), 2, 0, screen_width-64, screen_height/2+150+(i*100), screen_height/2+200+(i*100), asteroid, 10))
    L2_asteroids.append(Asteroid(screen_width/2+150, screen_height/2+160+(i*100), 2, 0, screen_width-64, screen_height/2+(i*100), screen_height/2+120+(i*100), asteroid, 10))

L2_keys = []
L2_keys.append(Key(25, screen_height/2, key))
L2_keys.append(Key(250, screen_height/4, key))
L2_keys.append(Key(screen_width-100, 400, key))
L2key_collected = [False, False, False]

# LEVEL THREE CONSTRUCTION
L3_asteroids = []
for i in range(10):
    L3_asteroids.append(Asteroid(120+(i*100), 110+(i*28), 0, 0, screen_width-64, 115, screen_height-64, asteroid, 7))

L3_keys = []
for i in range(5):
    L3_keys.append(Key(200+(i*200), screen_height-50, key))
L3key_collected = [False] * 5

# ======================================================== RUN GAME ===================================================*

# GAME INTERFACE
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            pygame.mixer.music.stop()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                speed_x = -5
            elif event.key == pygame.K_RIGHT:
                speed_x = 5
            elif event.key == pygame.K_UP:
                speed_y = -5
            elif event.key == pygame.K_DOWN:
                speed_y = 5
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                speed_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                speed_y = 0

    # move the stick figure according to the speed
    current_x += speed_x
    current_y += speed_y

    # screen boundaries -> make the ship (essentially) stop when it hits a wall
    if current_x <= 3 or current_x > screen_width - 100:
        speed_x *= -0.01
    if current_y <= 111 or current_y > screen_height-65:
        speed_y *= -0.01

    if level == 0:
        # create home/intro screen
        pygame.mouse.set_visible(True)
        screen.blit(intro_background, [0, 0])
        title = L_font.render("Are you scared?", True, WHITE)
        answerYes = font.render("Yes", True, GREEN)
        answerNo = font.render("No", True, RED)
        name = font3.render("Created by Alden Hinden-Stevenson", True, WHITE)
        screen.blit(navigate_title, [screen_width/4+25, screen_height/6])
        screen.blit(title, [screen_width/3, screen_height/2])
        screen.blit(answerYes, [screen_width/3-30, 2*screen_height/3])
        screen.blit(answerNo, [2*screen_width/3-30, 2*screen_height/3])
        screen.blit(name, [50, screen_height-50])

        pos = pygame.mouse.get_pos()
        x = pos[0]
        y = pos[1]
        if event.type == pygame.MOUSEBUTTONUP and x > 2*screen_width/3-40 and x < 2*screen_width/3+40 \
            and y > 2*screen_height/3 and y < 2*screen_height/3+50:
            pygame.mixer.music.load(game_music)
            pygame.mixer.music.play(-1, 0.4)
            level = 1
        elif event.type == pygame.MOUSEBUTTONUP and x > screen_width/3-40 and x < screen_width/3+60 \
            and y > 2*screen_height/3 and y < 2*screen_height/3+50:
            done = True

    if level > 0:
        # background for all levels
        screen.blit(background, (0, 0))

        # spawn character
        make_spaceship(screen, current_x, current_y)

        # setup level counter and death counter
        pygame.draw.rect(screen, BLACK, [0, 0, screen_width, 100])
        death_counter = L_font.render("Deaths: " + str(deaths), True, RED)
        level_num = L_font.render("Level: " + str(level), True, GREEN)
        screen.blit(death_counter, [900, 25])
        screen.blit(level_num, [100, 25])

        pygame.mouse.set_visible(False)

    if level == 1:
        # set target
        pygame.draw.rect(screen, GREEN, [screen_width-100, screen_height/2-150, 100, 300])
        instructions1 = font2.render("TRY TO", True, BLACK)
        instructions2 = font2.render("GET TO", True, BLACK)
        instructions3 = font2.render("HERE!!", True, BLACK)
        screen.blit(instructions1, [screen_width-90, screen_height/2-45])
        screen.blit(instructions2, [screen_width-90, screen_height/2-15])
        screen.blit(instructions3, [screen_width-90, screen_height/2+15])

        # set asteroids and keys
        for a in L1_asteroids:
            a.move()

        # collison test
        collided = False
        for a in L1_asteroids:
            if square((current_x) - (a.x)) + square((current_y) - (a.y)) <= 5100:
                collided = True
                current_x = 0
                current_y = screen_height / 2
                deaths += 1
                break

        # check for completion
        if current_x > screen_width - 150 and screen_height / 2 - 150 < current_y < screen_height / 2 + 150:
            current_x = screen_width / 2
            current_y = screen_height / 2
            level = 2

    if level == 2:
        # set target
        pygame.draw.rect(screen, GREEN, [screen_width - 150, screen_height-200, screen_width-10, screen_height])
        instructions1 = font2.render("Collect all", True, BLACK)
        instructions2 = font2.render("stars before", True, BLACK)
        instructions3 = font2.render("you arrive!", True, BLACK)
        screen.blit(instructions1, [screen_width - 145, screen_height-125])
        screen.blit(instructions2, [screen_width - 145, screen_height-100])
        screen.blit(instructions3, [screen_width -145, screen_height-75])



        # set asteroids and keys
        for a in L2_asteroids:
            a.move()
        for collected, key in zip(L2key_collected, L2_keys):
            if not collected:
                key.place()

        # collison test
        collided = False
        for a in L2_asteroids:
            if square((current_x) - (a.x)) + square((current_y) - (a.y)) <= 5100:
                collided = True
                current_x = screen_width / 2
                current_y = screen_height / 2
                L2key_collected = [False] * 3
                deaths += 1
                break

        # key collection test
        for i, k in enumerate(L2_keys):
            if square((current_x) - (k.x)) + square((current_y) - (k.y)) <= 5100:
                L2key_collected[i] = True
                break

        # check for completion
        if current_x > screen_width - 250 and current_y > screen_height - 260 and all(L2key_collected):
            current_x = 10
            current_y = 110
            level = 3

    if level == 3:
        # set target
        pygame.draw.rect(screen, GREEN, [screen_width - 150, screen_height - 200, screen_width, screen_height])

        # set asteroids and keys
        for a in L3_asteroids:
            a.move()
        for collected, key in zip(L3key_collected, L3_keys):
            if not collected:
                key.place()

        # collison test
        collided = False
        for a in L3_asteroids:
            if square((current_x) - (a.x)) + square((current_y) - (a.y)) <= 5100:
                collided = True
                current_x = 10
                current_y = 110
                L3key_collected = [False] * 5
                deaths += 1
                break

        # key collection test
        for i, k in enumerate(L3_keys):
            if square((current_x) - (k.x)) + square((current_y) - (k.y)) <= 5100:
                L3key_collected[i] = True
                break

        # check for completion
        if current_x > screen_width - 235 and current_y > screen_height - 260 and all(L3key_collected):
            # set lv4 spawn position
            level = 4

    if level == 4:
        # end screen
        pygame.mixer.music.stop()
        pygame.draw.rect(screen, GREEN, [300, 300, screen_width-600, 300])
        you_won = L_font.render("You Won! Congrats!", True, BLACK)
        death_total = font.render("Total Deaths: " + str(deaths), True, BLACK)
        screen.blit(you_won, [350, screen_height/2-35])
        screen.blit(death_total, [450, screen_height/2+75])

    # update the screen
    pygame.display.flip()
    clock.tick(30)
# end of main
pygame.QUIT