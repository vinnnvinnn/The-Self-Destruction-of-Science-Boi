import sys, pygame, os, random
os.environ['SDL_AUDIODRIVER'] = 'dsp'
pygame.init()
from pygame.locals import *
import time
# Set up a clock to control the speed of the animation
clock = pygame.time.Clock()

screen_size = 660, 380 #width, height
screen = pygame.display.set_mode(screen_size)

background = pygame.image.load('Background_1.png')

#Shortcuts for colors
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
cyan = (0, 255, 255)
purple = (255, 0, 255)
white = (255, 255, 255)
black = (0, 0, 0)
x_size = 70
background_x = 0
background_y = 0
level = 0
player_vx = 0
spawnpoint = [-25, 200]
player_x = spawnpoint[0]
player_y = spawnpoint[1]
player_vy = 0
move_right = True
move_left = True

def reset():
    global gravity; global MAX_SPEED; global ACCELERATION; global JUMP; global player; global x_size; global y_size; global reverse
    #Game Logic Parameters
    gravity = 10
    MAX_SPEED = 3
    ACCELERATION = 0.2
    JUMP = 5
    x_size = 70
    y_size = 45
    reverse = 1
    player = pygame.transform.scale(player, (x_size, y_size))

def scene(x): 
    global MAX_SPEED; global ACCELERATION; global JUMP; global player; global x_size; global y_size; global reverse; global player_x; global player_y; global background_x; global background_y; global background
    if x == 0:
        player_x = -25
        player_y = 200
        background = pygame.image.load('Background_1.png')
        background = pygame.transform.scale(background, (900, 650))           
        background_x = -100
        background_y = -75
    elif x == 1:
        player_x = -25
        player_y = 50
        background = pygame.image.load('Background_2.png')
        background = pygame.transform.scale(background, (990, 680))
        background_x = -175
        background_y = -180
        
        screen.blit(screen, (0, 0))
    elif x == 2:
        player_x = -25
        player_y = 200
        background = pygame.image.load('Background_3.png')
        background = pygame.transform.scale(background, (990, 700))
        screen.blit(background, (-100, -100))
        background_x = -165
        background_y = -200
    elif x == 3: # Big and slow
        screen.fill((200, 200, 200))
        background = pygame.image.load('Strong_1.png')
        background = pygame.transform.scale(background, (660, 380))
        background = screen.blit(background ,(10, -30))
        pygame.display.update()
        pygame.time.delay(3000)
        screen.fill((200, 200, 200))
        background = pygame.image.load('Strong_2.png')
        background = pygame.transform.scale(background, (660, 380))
        background = screen.blit(background, (0, -40)) 
        pygame.display.update()
        pygame.time.delay(3000)
        screen.fill((200, 200, 200))
        background = pygame.image.load('Strong_3.png')
        background = pygame.transform.scale(background, (660, 380))
        background = screen.blit(background, (-20, -40)) 
        pygame.display.update()
        pygame.time.delay(3000)
        MAX_SPEED = 2
        JUMP = 5
        x_size = 140
        y_size = 90
        player_x = -25
        player_y = 200
        player = pygame.transform.scale(player, (x_size, y_size))
        background = pygame.image.load('Background.png')
        background = pygame.transform.scale(background, (900, 650))           
        background_x = -70
        background_y = -100

    elif x == 4 : # Reverse controls
        player_x = 50
        player_y = 200
        reverse = -1
        screen.fill((200, 200, 200))
        background = pygame.image.load('Smart.png')
        background = pygame.transform.scale(background, (330, 190))
        background = screen.blit(background ,(150, 100))
        pygame.display.update()
        pygame.time.delay(3000)
        screen.fill((200, 200, 200))
        background = pygame.image.load('Smart_2.png')
        background = pygame.transform.scale(background, (330, 190))
        background = screen.blit(background, (150, 100)) 
        pygame.display.update()
        pygame.time.delay(3000)
        screen.fill((200, 200, 200))
        background = pygame.image.load('Background.png')
        background = pygame.transform.scale(background, (900, 650))           
        background_x = -70
        background_y = -100

def die():
    global player_x; global player_y; global spawnpoint; global level
    screen.fill((0, 0, 0))
    pygame.display.update()
    pygame.time.delay(500)
    scene(level)
    
#Images
player = pygame.image.load('Player.png')

ground = pygame.image.load('Ground.png')
ground = pygame.transform.scale(ground, (66, 38))

ground_2 = pygame.image.load('Ground_2.png')
ground_2 = pygame.transform.scale(ground_2, (66, 38))

poison = pygame.image.load('Poison.png')
poison = pygame.transform.scale(poison, (66, 38))

poison_2 = pygame.image.load('Poison_2.png')
poison_2 = pygame.transform.scale(poison_2, (66, 38))

platform = pygame.image.load('Platform.png')
platform = pygame.transform.scale(platform, (66, 38))

platform_2 = pygame.image.load('Platform_2.png')
platform_2 = pygame.transform.scale(platform_2, (22, 38))

gravity = pygame.image.load('Gravity.png')
gravity = pygame.transform.scale(gravity, (66, 38))



ground_x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29 , 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]
                                
ground_y = [9, 9, 9, 9, 8, 7, 6, 5, 4, 4, 4, 5, 6, 7, 8, 9, 9, 9, 9, 9, 9, 8, 9, 7, 9, 6, 9, 7, 9, 8, 9, 8, 7, 6, 9, 8, 9, 9, 9, 9, 9, 8, 7, 8, 7, 6, 5, 4, 5, 6]
ground_type = ["g", "g", "g", "s", "s", "s", "s", "s", "g", "g", "g", "po", "g", "po", "g", "g", "g", "g", "g", "g", "g", "g", "po", "g", "po", "g", "po", "g", "po", "g", "g", "g", "g", "g", "po", "g", "g", "g", "g", "g", "g", "g", "g", "g", "g", "g", "g", "g", "g", "g"]

direction = "Right"
falling = False

pressed_keys = []
def touchingGround():
    global player_y
    global player_x
    global player_vx
    global direction
    global move_right
    global move_left
    global falling
    ground = False
    for i in range(len(ground_x)):
        if (player_x + x_size/2 <= ground_x[i] * 66 + 66) and (player_x + x_size >= ground_x[i] * 66):
            if player_y + y_size + 2 >= ground_y[i] * 38:
                if ground_type[i] == "po":
                    die()
                else:
                    if ((player_y + y_size + 2) - (ground_y[i] * 38) > 20):
                        player_vx = 0
                        if direction == "Right":
                            player_x = ground_x[i] * 66 - 45 * (x_size/70)
                            move_right = False
                        else:
                            player_x = ground_x[i] * 66 + 38 * (x_size/70)
                            move_left = False
                    else:
                        player_y = ground_y[i] * 38 - y_size + 2
                ground = True
            break
    return(ground)

def newLevel():
    global player_x; global player_y; global player_vy; global move_right; global move_left; global level
    player_vy = 0
    move_right = True
    move_left = True
    a = 0
    for i in range(len(ground_x)):

        if (ground_x[i-a]) <= 9:
            ground_x.pop(0)
            ground_y.pop(0)
            ground_type.pop(0)
            a = a+1
        else:
            ground_x[i-a] -= 10

    reset()
    level += 1
    scene(level)

reset()
scene(level)
while True:
    screen.fill((65, 80, 65))
    background_1 = screen.blit(background, (background_x, background_y))
    
    # Physics Engine:
    pressed_keys = pygame.key.get_pressed()
    events = pygame.event.get()

    if reverse == 1:
        if pressed_keys[pygame.K_UP]:
            if touchingGround() == True:
                player_vy = -JUMP
    else:
        if pressed_keys[pygame.K_DOWN]:
            if touchingGround() == True:
                player_vy = -JUMP

    if pressed_keys[pygame.K_LEFT]:
        direction = "Left"
        move_right = True
        if move_left == True:
            if player_vx <= -MAX_SPEED * reverse:
                player_vx = -MAX_SPEED * reverse
            else:
                player_vx -= ACCELERATION * reverse
    elif player_vx < 0 and pressed_keys[pygame.K_RIGHT]==False:
        player_vx += ACCELERATION * reverse

    if pressed_keys[pygame.K_RIGHT]:
        direction = "Right"
        move_left = True
        if move_right == True:
            if player_vx >= MAX_SPEED * reverse:
                player_vx = MAX_SPEED * reverse
            else:
                player_vx += ACCELERATION * reverse
    elif player_vx > 0 and pressed_keys[pygame.K_LEFT]==False:
        player_vx = 0

    player_x += player_vx
    player_y += player_vy
    player_pos = (player_x, player_y)
    player_rect = screen.blit(player, player_pos)

    if touchingGround() == False:
        player_vy += 0.25
    else:
        player_vy = 0

    for i in range(len(ground_x)):
        if ground_x[i] < 10:
            if ground_type[i] == "g":
                ground_1 = screen.blit(ground, (ground_x[i] * 66, ground_y[i] * 38)) 
                if ground_y[i] != 9:
                    for a in range(9 - ground_y[i]):
                        ground_3 = screen.blit(ground_2, (ground_x[i] * 66, (ground_y[i]  + a + 1) * 38))
            elif ground_type[i] == "po":
                poison_1 = screen.blit(poison, (ground_x[i] * 66, ground_y[i] * 38))
                if ground_y[i] != 9:
                    for a in range(9 - ground_y[i]):
                        poison_3 = screen.blit(poison_2, (ground_x[i] * 66, (ground_y[i]  + a + 1) * 38))
            elif ground_type[i] == "s":
                platform_1 = screen.blit(platform, (ground_x[i] * 66, ground_y[i] * 38))
                if ground_y[i] != 9:
                    for a in range(9 - ground_y[i]):
                        platform_3 = screen.blit(platform_2, (ground_x[i] * 66 + 22, (ground_y[i]  + a + 1) * 38))
        else:
            break
    player_1 = screen.blit(player, (player_x, player_y))


    if player_x >= 630:
        newLevel()
    pygame.display.update()
    clock.tick(60)
