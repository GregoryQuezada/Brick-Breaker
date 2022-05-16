"""
To do:
Greg + Zach:
 - Ball physics and bar movement - Speed variables, direction, angles, etc.
 - Help organize code into a template and stuff
 - Test collision mechanics and related topics

Problem Statement: Create a game of breakout in Python.
"""

import pygame
import sys
from pygame.locals import *
import math

pygame.init()

# Width and height
width = 416
height = 630

fpsClock = pygame.time.Clock()
FPS = 60
display_surface = pygame.display.set_mode((width, height))


# Colors
white = (200, 200, 200)
black = (0, 0, 0)

# Directions
LEFT = 'left'
RIGHT = 'right'

# FontObject (You win!)
fontObj1 = pygame.font.Font("freesansbold.ttf", 32)
textSurfaceObj1 = fontObj1.render("You win!", True, white)
textRectObj1 = textSurfaceObj1.get_rect()
textRectObj1.center = (200, 300)

# FontObject (You lose!)
fontObj2 = pygame.font.Font("freesansbold.ttf", 32)
textSurfaceObj2 = fontObj2.render("You lose!", True, white)
textRectObj2 = textSurfaceObj2.get_rect()
textRectObj2.center = (200, 300)

# Creates groups for different sprites
sprites = []
tiles = []


# Ball class
class Ball(pygame.sprite.Sprite):
    image = pygame.image.load("Ball.png")

    #Ball's speed in pixels
    speed = 8.0

    #Ball's floating point representation
    x = 0.0
    y = 280.0

    #Direction in degrees
    direction = 200

    def __init__(self):
        sprites.append(self)

        # Call the Sprite constructor
        pygame.sprite.Sprite.__init__(self)

        # Create a block and load image
        self.image = pygame.image.load("Ball.png")

        # self.image = pygame.Surface([self.width, self.height])

        # Get dimensions
        #self.rect = self.image.get_rect()

        self.rect = self.image.get_rect(topleft=((width / 2) - 32, height - 96))

        # Get height and width of screen
        '''self.screenheight = display_surface.get_width()
        self.screenwidth = display_surface.get_height()'''

    def bounce(self, diff):
        # This will bounce ball off horizontal surface

        self.direction = (180 - self.direction) % 360
        self.direction -= diff

    def update(self):
        # Updates position of ball
        direction_radians = math.radians(self.direction)

        # Changes x and y coordinates based on speed and direction
        self.x += self.speed * math.sin(direction_radians)
        self.y -= self.speed * math.cos(direction_radians)

        # Moves image to x and y coordinates
        self.rect.x = self.x
        self.rect.y = self.y

        # Bounces off top of screen
        if self.y <= 0:
            self.bounce(0)
            self.y = 1

        # Bounces off left side of screen
        if self.x <= 0:
            self.direction = (360 - self.direction) % 360
            self.x = 1

        # Bounces off right side of screen
        if self.x > width - self.rect.width:
            self.direction = (360 - self.direction) % 360
            self.x = width - self.rect.width - 1

        # Checks if ball fell off the bottom of screen
        if self.y > height:
            return True
        else:
            return False

# Bar class
class Bar(pygame.sprite.Sprite):
    image = pygame.image.load("Bar.png")

    def __init__(self):
        sprites.append(self)

        # Call the Sprite constructor
        pygame.sprite.Sprite.__init__(self)

        # Create a block and load image
        self.image = pygame.image.load("Bar.png")

        # Get dimensions
        self.rect = self.image.get_rect(topleft=((width / 2) - 40, height - 28))

        # Get height and width of screen
     #   self.screenheight = display_surface.get_width()
     #   self.screenwidth = display_surface.get_height()

    def update(self):
        # Update the movement of the bar according to user input
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 4
        if keys[pygame.K_RIGHT]:
            self.rect.x += 4

        # Ensures that bar doesn't go off the screen
        if self.rect.x > width - self.rect.width:
            self.rect.x = width - self.rect.width

        if self.rect.x < 0:
            self.rect.x = 0

# Green Tile class
class GreenTile(pygame.sprite.Sprite):
    image = pygame.image.load("tileGR.png")

    def __init__(self):
        tiles.append(self)

        # Call the Sprite constructor
        pygame.sprite.Sprite.__init__(self)

        # Create a block and load image
        self.image = pygame.image.load("tileGR.png")

        # Get dimensions
        self.rect = self.image.get_rect()


# Red Tile class
class RedTile(pygame.sprite.Sprite):
    image = pygame.image.load("tileRD.png")

    def __init__(self):
        tiles.append(self)

        # Call the Sprite constructor
        pygame.sprite.Sprite.__init__(self)

        # Create a block and load image
        self.image = pygame.image.load("tileRD.png")

        # Get dimensions
        self.rect = self.image.get_rect()


# Blue Tile class
class BlueTile(pygame.sprite.Sprite):
    image = pygame.image.load("tileBL.png")

    def __init__(self):
        tiles.append(self)

        # Call the Sprite constructor
        pygame.sprite.Sprite.__init__(self)

        # Create a block and load image
        self.image = pygame.image.load("tileBL.png")

        # Get dimensions
        self.rect = self.image.get_rect()


# Yellow Tile class
class YellowTile(pygame.sprite.Sprite):
    image = pygame.image.load("tileYW.png")

    def __init__(self):
        tiles.append(self)

        # Call the Sprite constructor
        pygame.sprite.Sprite.__init__(self)

        # Create a block and load image
        self.image = pygame.image.load("tileYW.png")

        # Get dimensions
        self.rect = self.image.get_rect()
'''
# INITIALIZE VARIABLES
count = 24  # Number of tiles to break'''

ball = Ball()  # Initialises ball
bar = Bar()  # Initialises bar

'''
rt = RedTile()  # Initialises red tiles
yt = YellowTile()  # Initialises yellow tiles
gt = GreenTile()  # Initialises green tiles
bt = BlueTile()  # Initialises blue tiles

tile = {rt, yt, gt, bt}'''

# Create sprite list
blocks = pygame.sprite.Group()

row = 0   # Row Count

'''for i in tile:
    numy = 5 + (row * 68)   # Changes row position
    numx = 5
    i.rect.x = numx
    i.rect.y = numy
    while numx <= 400:
        display_surface.blit(i.image, i.rect) # Adds image
        blocks.add(i)
        numx += 68
        i.rect.x = numx
    row += 1
    numy += 68'''

# Creation of separate rows
numy = 5 + (row * 68)
numx = 5

while numx <= 400:
    block = RedTile()
    block.rect.x = numx
    block.rect.y = numy
    blocks.add(block)
    numx += 68

numy = 5 + ((row + 1) * 68)
numx = 5

while numx <= 400:
    block = YellowTile()
    block.rect.x = numx
    block.rect.y = numy
    blocks.add(block)
    numx += 68

numy = 5 + ((row + 2) * 68)
numx = 5

while numx <= 400:
    block = GreenTile()
    block.rect.x = numx
    block.rect.y = numy
    blocks.add(block)
    numx += 68

numy = 5 + ((row + 3) * 68)
numx = 5

while numx <= 400:
    block = BlueTile()
    block.rect.x = numx
    block.rect.y = numy
    blocks.add(block)
    numx += 68


# Main method
def main():
    pygame.init()  # Initialises pygame

    global display_surface

    # Window Size and Display;
    display_surface = pygame.display.set_mode((width, height))  # 415, 630
    # (400, 400) is window size by width and height, respectively
    pygame.display.set_caption("Test!")  # Title Bar


    while True:
        run_game()


# Method for checking collisions
def check_brick_collision(sprite1, sprite2):
    # Check for collisions between the ball and the blocks
    dead = pygame.sprite.spritecollide(sprite1, sprite2, True)

    # If we actually hit a block, bounce the ball
    if len(dead) > 0:
        ball.bounce(0)

        # Game ends if all the blocks are gone
        if len(blocks) == 0:
            return True
        else:
            return False





# Game method
def run_game():
    game_over = False
    game_win = False
    '''# INITIALIZE VARIABLES
    count = 24   # Number of tiles to break

    ball = Ball()   # Initialises ball
    bar = Bar()   # Initialises bar

    rt = RedTile()   # Initialises red tiles
    yt = YellowTile()   # Initialises yellow tiles
    gt = GreenTile()   # Initialises green tiles
    bt = BlueTile()   # Initialises blue tiles

    tile = {rt, yt, gt, bt}'''

    # speed = [2, 2]

    # ball_rect = ball.rect


    while not False:  # main game loop
        display_surface.fill(black)

        '''row = 0   # Row Count
        for i in tile:
            numy = 5 + (row * 68)   # Changes row position
            numx = 5
            i.rect.x = numx
            i.rect.y = numy
            while numx <= 400:
                display_surface.blit(i.image, i.rect)   # Adds image
                blocks.add(i)
                numx += 68
                i.rect.x = numx
            row += 1
            numy += 68'''

        # Adds ball
        display_surface.blit(ball.image, ball.rect)

        # Adds bar
        display_surface.blit(bar.image, bar.rect)

        blocks.draw(display_surface)

        # Update ball and bar if game is not over
        if not (game_win or game_over):
            bar.update()
            game_over = ball.update()

        # If you lose
        if game_over:
            display_surface.blit(textSurfaceObj2, textRectObj2)
            #pygame.quit()

        # If you win
        if game_win:
            display_surface.blit(textSurfaceObj1, textRectObj1)

        for event in pygame.event.get():
            if event.type == QUIT:  # If you click exit
                pygame.quit()
                sys.exit()  # System exits

        # See if the ball hits the player paddle
        if pygame.sprite.collide_rect(bar, ball):
            # The 'diff' lets you try to bounce the ball left or right
            # depending where on the paddle you hit it
            diff = (bar.rect.x + bar.rect.left / 2) - (ball.rect.x + ball.rect.left / 2)

            # Set the ball's y position in case
            # we hit the ball on the edge of the paddle
            ball.rect.y = height - bar.rect.height - ball.rect.height - 1
            ball.bounce(diff)

        if check_brick_collision(ball, blocks):
            game_win = True


        # Updates window
        fpsClock.tick(FPS)
        pygame.display.update()

main()
