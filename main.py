import pygame, sys, random
from pygame.locals import *
pygame.init()

score = 0
clock = pygame.time.Clock()
# CREATING CANVAS
DISPLAY = pygame.display.set_mode((1080, 720))

# TITLE OF CANVAS
pygame.display.set_caption("Game(WIP)")

WHITE = (255,255,255)

Player = pygame.image.load('Assets/Player.png')
enemy = pygame.image.load('Assets/enemy.png')
bullet = pygame.image.load('Assets/Bullet.png')
x_position = 1080 / 2 - 32/2
y_position = 720 / 2 - 32/2

random_x_position = random.randint(0,100)
random_y_position = random.randint(-64, -25)
bulletypos = y_position
bulletxpos = x_position
print(random_x_position)
print(random_y_position)
def spawn_enemy():
    DISPLAY.blit(enemy, (random_x_position, random_y_position))
#DISPLAY.blit(enemy, (enemy_x_position, enemy_y_position))
range(2,3)
def spawn_bullet():
    DISPLAY.blit(bullet, (bulletxpos, bulletypos))

print("TAP SPACE TO SHOOT BULLET")

while True:
    
    clock.tick(60)
    
    
    for event in pygame.event.get():
        if event.type==QUIT:
            
            pygame.quit()
            sys.exit()
            
    
    #
    keys = pygame.key.get_pressed() #key input
    if keys[pygame.K_RIGHT]:
        x_position = x_position + 5
        bulletxpos = x_position
    if keys[pygame.K_LEFT]:
        x_position = x_position - 5
        bulletxpos = x_position
   # if keys[pygame.K_DOWN]:
   #     y_position = y_position + 5
   # if keys[pygame.K_UP]:
   #     y_position = y_position - 5
    
    if x_position + 32 > random_x_position and x_position < random_x_position + 32 and y_position + 32 >random_y_position and y_position < random_y_position + 32:
        random_x_position = random.randint(0,1000)
        random_y_position = random.randint(-64, -25)
        score = 0
        print(score)
    if random_y_position > 344:
        score = 0
        print(score)
        
    if random_y_position > 344:
        random_x_position = random.randint(0,1000)
        random_y_position = random.randint(-64, -25) 
    if x_position > 1080:
        x_position = 14
    if x_position < 0:
        x_position = 1044   
    random_y_position = random_y_position + 1
    DISPLAY.fill(WHITE)
    DISPLAY.blit(Player, (x_position,y_position))
    DISPLAY.blit(enemy, (random_x_position, random_y_position))
    spawn_enemy()
    #
    
    if keys[pygame.K_ASTERISK]:
        print(x_position)
        print(y_position)
    
    if keys[pygame.K_CAPSLOCK]:
        x_position = 0
        y_position = 0
    
    if keys[pygame.K_j]:
        x_position = 70
        y_position = 70
        print("heheheheheh, don't press J ( Also why does this do the repeat thing? )")
    if keys[pygame.K_SPACE]:
        spawn_bullet()
    bulletypos=bulletypos-10
    DISPLAY.blit(bullet, (bulletxpos, bulletypos))
        
    if bulletypos < -56:
        bulletypos = y_position
        DISPLAY.blit(bullet, (bulletxpos, bulletypos))
    if bulletxpos + 32 > random_x_position and bulletxpos < random_x_position + 32 and bulletypos + 32 >random_y_position and bulletypos < random_y_position + 32 :
        score = score+1
        random_x_position = random.randint(0,1000)
        random_y_position = random.randint(-64, -25)
        print(score)
    pygame.display.update()




