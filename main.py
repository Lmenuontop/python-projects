import pygame, sys, random
from pygame.locals import *
pygame.init()

score = 1  
print(score)
clock = pygame.time.Clock()

# CREATING CANVAS
DISPLAY = pygame.display.set_mode((1080, 720))

# TITLE OF CANVAS
pygame.display.set_caption("Game(WIP)")

WHITE = (255, 255, 255)

Player = pygame.image.load('Assets/Player.png')
enemy = pygame.image.load('Assets/enemy.png')
bullet = pygame.image.load('Assets/Bullet.png')

x_position = 1080 / 2 - 32 / 2
y_position = 720 / 2 - 32 / 2

random_x_position = random.randint(0, 1000)
random_y_position = random.randint(-64, -25)

bullet_fired = False
bulletypos = -10  # Set bullet y position off-screen initially
bulletxpos = 0

def spawn_enemy():
    DISPLAY.blit(enemy, (random_x_position, random_y_position))

def spawn_bullet():
    DISPLAY.blit(bullet, (bulletxpos, bulletypos))

print("TAP SPACE TO SHOOT BULLET")
print("THE NUMBERS ARE YOUR SCORE, YOU START WITH 1")
print("IF YOUR SCORE BECOMES ZERO, YOU LOSE")

while True:
    
    clock.tick(60)
    
    for event in pygame.event.get():
        if event.type == QUIT or score == 0:
            print("Bye")            
            pygame.quit()
            sys.exit()
    
    # Key input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        x_position = x_position + 5
    if keys[pygame.K_LEFT]:
        x_position = x_position - 5
    
    if x_position + 32 > random_x_position and x_position < random_x_position + 32 and y_position + 32 > random_y_position and y_position < random_y_position + 32:
        random_x_position = random.randint(0, 1000)
        random_y_position = random.randint(-64, -25)
        score = 0
        print(score)

    if random_y_position > 344:
        score = 0
        print(score)

    if random_y_position > 344:
        random_x_position = random.randint(0, 1000)
        random_y_position = random.randint(-64, -25)
    
    if x_position > 1080:
        x_position = 14
    if x_position < 0:
        x_position = 1044   
    
    random_y_position = random_y_position + 1

    DISPLAY.fill(WHITE)
    DISPLAY.blit(Player, (x_position, y_position))
    DISPLAY.blit(enemy, (random_x_position, random_y_position))
    spawn_enemy()
#debug
    if keys[pygame.K_ASTERISK]:
        print(x_position)
        print(y_position)
#debug
    if keys[pygame.K_CAPSLOCK]:
        x_position = 0
        y_position = 0

    if keys[pygame.K_SPACE] and not bullet_fired:
        bullet_fired = True
        bulletxpos = x_position  # Set bullet's x position to player's current x position
        bulletypos = y_position - 10  # Start bullet just above the player
    
    if bullet_fired:
        # Move the bullet upwards (no change in x position)
        bulletypos -= 10
        spawn_bullet()

        if bulletypos < -56:
            bullet_fired = False  # Reset the bullet once it goes off-screen
            bulletypos = -10  # Reset y position off-screen

        # Check for bullet collision with the enemy
        if bulletxpos + 32 > random_x_position and bulletxpos < random_x_position + 32 and bulletypos + 32 > random_y_position and bulletypos < random_y_position + 32:
            score += 1
            random_x_position = random.randint(0, 1000)
            random_y_position = random.randint(-64, -25)
            bullet_fired = False
            print(score)
    
    pygame.display.update()

