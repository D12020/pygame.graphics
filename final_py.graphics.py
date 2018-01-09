# Imports
import pygame
import math
import random

# Initialize game engine
pygame.init()


# Window
SIZE = (800, 600)
TITLE = "My Awesome Picture"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)


# Timer
clock = pygame.time.Clock()
refresh_rate = 60


# Colors
RED = (255, 0, 0)
GREEN = (68, 244, 65)
BLUE = (66, 134, 244)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ORANGE = (255, 125 , 0)
YELLOW =(244, 235, 66)
BROWN =(86, 57, 40)

'''make snow'''
snow = []
for i in range (200):
    x= random.randrange(0,800)
    y= random.randrange(0,400)
    r= random.randrange(1, 5)
    snow.append([x,y,r,r])


def draw_cloud(x,y):
    pygame.draw.ellipse(screen, WHITE, [x,y + 20,40,40])
    pygame.draw.ellipse(screen, WHITE, [x + 60, y +20, 40,40])
    pygame.draw.ellipse(screen, WHITE, [x + 20, y + 10,25,25])
    pygame.draw.ellipse(screen, WHITE, [x + 35, y, 50 ,50])
    pygame.draw.rect(screen, WHITE, [x + 20, y + 20, 60, 40])

def trees(w,x,y,z):
    pygame.draw.rect(screen, BROWN,[x,y,50,100])
    pygame.draw.ellipse(screen, GREEN,[20,y+250,20,100])


    

# Game loop
done = False

while not done:
    # Event processing (React to key presses, mouse clicks, etc.)
    ''' for now, we'll just check to see if the X is clicked '''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True


    # Game logic (Check for collisions, update points, etc.)
    ''' leave this section alone for now ''' 

    # Drawing code (Describe the picture. It isn't actually drawn yet.)
    screen.fill(BLUE)
    pygame.draw.rect(screen, GREEN, [0, 450, 1300, 300])
    pygame.draw.rect(screen, ORANGE, [400, 250, 300, 200])
    pygame.draw.polygon(screen, BLACK, [[350, 250], [550,150], [750, 250]])
    pygame.draw.rect(screen, YELLOW, [525, 350, 55, 100])
    pygame.draw.rect(screen, WHITE,[420, 275, 75, 75])
    pygame.draw.rect(screen, WHITE,[600, 275, 75, 75])
    pygame.draw.line(screen, BLACK, [457, 275], [457 ,350], 2)
    pygame.draw.line(screen, BLACK,[495,312.5], [420, 312.5], 2)
    pygame.draw.line(screen, BLACK,[637, 275], [637, 350], 2)
    pygame.draw.line(screen, BLACK,[675, 313], [600,313], 2)
    draw_cloud(50,200)
    draw_cloud(250,75)
    draw_cloud(350,125)
    draw_cloud(450,50)
    draw_cloud(650,100)

    '''tree'''
    trees(50,450,100,100)

    '''snow'''
    for s in snow:
        pygame.draw.ellipse(screen,WHITE,s)

    y = 380
    for x in range(5, 800, 30):
        post = [[x+5, y],[x+10, y+5],[x+10, y+80],[x, y+80], [x, y+5]]
        pygame.draw.polygon(screen, WHITE, post)
        
    pygame.draw.rect(screen, WHITE, [0, y+10, 800, 5])
    pygame.draw.rect(screen, WHITE, [0, y+50, 800, 5])
    

    ''' angles for arcs are measured in radians (a pre-cal topic) '''
    pygame.draw.arc(screen, YELLOW, [50, 50, 150, 150],0, math.pi*2,75)


    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()


    # Limit refresh rate of game loop 
    clock.tick(refresh_rate)


# Close window and quit
pygame.quit()
