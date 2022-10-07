import pygame
pygame.init()
win = pygame.display.set_mode((500, 450))
pygame.display.set_caption("First game")
## Import the background of the game
bg = pygame.image.load('game_item//bg.jpg')
## Import the character images :
music = pygame.mixer.Sound("game_item//daredevil.mp3")
volume = .5

# pygame.mixer.Sound.play(music)

# right walk frames
walkRight = [pygame.image.load('game_item//R1.png'),
             pygame.image.load('game_item//R2.png'),
             pygame.image.load('game_item//R3.png'),
             pygame.image.load('game_item//R4.png'),
             pygame.image.load('game_item//R5.png'),
             pygame.image.load('game_item//R6.png'),
             pygame.image.load('game_item//R7.png'),
             pygame.image.load('game_item//R8.png'),
             pygame.image.load('game_item//R9.png')]

# left walk frames
walkLeft = [pygame.image.load('game_item//L1.png'),
            pygame.image.load('game_item//L2.png'),
            pygame.image.load('game_item//L3.png'),
            pygame.image.load('game_item//L4.png'),
            pygame.image.load('game_item//L5.png'),
            pygame.image.load('game_item//L6.png'),
            pygame.image.load('game_item//L7.png'),
            pygame.image.load('game_item//L8.png'),
            pygame.image.load('game_item//L9.png')]

char = pygame.image.load('game_item//standing.png')

screen_y = 500
screen_x = 450
clock = pygame.time.Clock()
x = 50
y = 390
width = 64
height = 64
vel = 5
jump = False
jump_count = 10
run = True
left  = False
right = False
walkcount = 0

# draw the WINDOW and Direction function

def drawgamewindow():
    # drawing a character
    global walkcount
    win.blit(bg, (0, 0)) #cause of a picture background
    if walkcount +1 >= 27:
        walkcount = 0
    if left :
        win.blit(walkLeft[walkcount//3],(x,y))
        walkcount = walkcount + 1
    elif right:
        win.blit(walkRight[walkcount//3], (x,y))
        walkcount = walkcount + 1
    else:
        win.blit(char,(x,y))
    pygame.display.update()

## Main loop for command

while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    #making a list for pressed keys
    keys = pygame.key.get_pressed()
    # x is less than velocity because if i move the object left it becomes negative x co-ordinate
    if keys[pygame.K_LEFT] and x > vel:
        left = True
        right = False
        x = x - vel
    # x < 500 cause screenlenght and pixel of character
    elif keys[pygame.K_RIGHT] and x < screen_x - width:
        right = True
        left = False
        x = x + vel
    elif keys[pygame.K_ESCAPE]:
        pygame.quit()
    elif keys[pygame.K_s]:
        pygame.mixer.Sound.play(music)
    elif keys[pygame.K_m]:
        pygame.mixer.Sound.stop(music)
    elif keys[pygame.K_UP] and volume <= 1.0:
        volume = volume + .1
        pygame.mixer.Sound.set_volume(music, volume)
    elif keys[pygame.K_DOWN] and volume >= 0.0:
        volume = volume - .1
        pygame.mixer.Sound.set_volume(music, volume)
    else:
        right = False
        left  = False
        walkcount = 0

    # when jumping user should not go up or down
    if not(jump):
        if keys[pygame.K_SPACE]:
            jump = True
            right = False
            left = False
            walkcount = 0
    else:
        if jump_count >= -10:
            # set a loop for jumping down in terms of negative
            neg = 1
            if jump_count < 0:
                neg = -1
            y -= (jump_count ** 2)/2* neg   # user jumps then decreases speed for H
            jump_count = jump_count - 1
        else:
            jump = False
            jump_count = 10

    drawgamewindow()
pygame.quit()