
import pygame
import random
import time
import sys

pygame.init()

# Load images
m = 20  # Size of the snake segments and food
Imgbody = pygame.transform.scale(pygame.image.load('trom1.jpg'), (m, m))
Imghead = pygame.transform.scale(pygame.image.load('trom.jpg'), (m, m))
Imgfood = pygame.transform.scale(pygame.image.load('apple.jpg'), (m, m))

# Create game window
gameSurface = pygame.display.set_mode((735, 475))
pygame.display.set_caption('Snake!')

# Colors
red = pygame.Color(255, 0, 0)
blue = pygame.Color(65, 105, 255)
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
gray = pygame.Color(128, 128, 128)

# Initial game variables
snakepos = [100, 60]
snakebody = [[100, 60], [80, 60], [60, 60]]
foodx = random.randrange(1, 71)
foody = random.randrange(1, 45)
if foodx % 2 != 0:
    foodx += 1
if foody % 2 != 0:
    foody += 1
foodpos = [foodx * 10, foody * 10]
foodflat = True
direction = 'RIGHT'
changeto = direction
score = 0

# Game over function
def game_over():
    gfont = pygame.font.SysFont('consolas', 40)
    gsurf = gfont.render('Game Over!', True, red)
    grect = gsurf.get_rect()
    grect.midtop = (360, 150)
    gameSurface.blit(gsurf, grect)
    show_score(0)
    pygame.display.flip()
    time.sleep(5)
    pygame.quit()
    sys.exit()

# Show score function
def show_score(choice=1):
    sfont = pygame.font.SysFont('consolas', 20)
    ssurf = sfont.render('Score: {0}'.format(score), True, black)
    srect = ssurf.get_rect()
    if choice == 1:
        srect.midtop = (70, 20)
    else:
        srect.midtop = (360, 230)
    gameSurface.blit(ssurf, srect)

# Main game loop
while True:
    pygame.time.delay(200)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                changeto = 'RIGHT'
            if event.key == pygame.K_LEFT:
                changeto = 'LEFT'
            if event.key == pygame.K_UP:
                changeto = 'UP'
            if event.key == pygame.K_DOWN:
                changeto = 'DOWN'
            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(pygame.QUIT))

    # Validate direction
    if changeto == 'RIGHT' and not direction == 'LEFT':
        direction = 'RIGHT'
    if changeto == 'LEFT' and not direction == 'RIGHT':
        direction = 'LEFT'
    if changeto == 'UP' and not direction == 'DOWN':
        direction = 'UP'
    if changeto == 'DOWN' and not direction == 'UP':
        direction = 'DOWN'

    # Update snake position
    if direction == 'RIGHT':
        snakepos[0] += m
    if direction == 'LEFT':
        snakepos[0] -= m
    if direction == 'UP':
        snakepos[1] -= m
    if direction == 'DOWN':
        snakepos[1] += m

    # Snake body growing mechanism
    snakebody.insert(0, list(snakepos))
    if snakepos[0] == foodpos[0] and snakepos[1] == foodpos[1]:
        score += 1
        foodflat = False
    else:
        snakebody.pop()

    # Spawning food on the screen
    if not foodflat:
        foodx = random.randrange(1, 71)
        foody = random.randrange(1, 45)
        if foodx % 2 != 0:
            foodx += 1
        if foody % 2 != 0:
            foody += 1
        foodpos = [foodx * 10, foody * 10]
        foodflat = True

    # Draw everything on the game window
    gameSurface.fill(white)
    for pos in snakebody:
        gameSurface.blit(Imgbody, pygame.Rect(pos[0], pos[1], m, m))
    gameSurface.blit(Imghead, pygame.Rect(snakebody[0][0], snakebody[0][1], m, m))
    gameSurface.blit(Imgfood, pygame.Rect(foodpos[0], foodpos[1], m, m))

    # Check for game over conditions
    if snakepos[0] > 710 or snakepos[0] < 10 or snakepos[1] > 450 or snakepos[1] < 10:
        game_over()
    for b in snakebody[1:]:
        if snakepos[0] == b[0] and snakepos[1] == b[1]:
            game_over()

    # Draw the game border
    pygame.draw.rect(gameSurface, gray, (10, 10, 715, 455), 2)
    show_score()
    pygame.display.flip()
