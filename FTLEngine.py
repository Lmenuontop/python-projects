import pygame
import sys
import random
from pygame.locals import *
# Initialize Pygame
pygame.init()

# Define global variables
WHITE = (255, 255, 255)
DISPLAY = None
player_x = None
player_y = None
velocity = 0
def create_display(x, y):
    global DISPLAY
    DISPLAY = pygame.display.set_mode((x, y))

def set_display_title(title):
    pygame.display.set_caption(title)

def load_asset(asset_name, directory):
    return pygame.image.load(f"{directory}/{asset_name}")

def add_default_movement(asset_to_move_x_pos, asset_to_move_y_pos):
    keys = pygame.key.get_pressed()
    if keys[K_UP]:
        asset_to_move_y_pos -= 1
    elif keys[K_DOWN]:
        asset_to_move_y_pos += 1
    elif keys[K_LEFT]:
        asset_to_move_x_pos -= 1
    elif keys[K_RIGHT]:
        asset_to_move_x_pos += 1
    return asset_to_move_x_pos, asset_to_move_y_pos
def add_custom_movement(asset_to_move_x_pos, asset_to_move_y_pos, key_up, key_down, key_left, key_right):
    keys = pygame.key.get_pressed()
    if keys[key_up]:
        asset_to_move_y_pos -= 1
    elif keys[key_down]:
        asset_to_move_y_pos += 1
    elif keys[key_left]:
        asset_to_move_x_pos -= 1
    elif keys[key_right]:
        asset_to_move_x_pos += 1
    return asset_to_move_x_pos, asset_to_move_y_pos
def draw_sprite(asset_name_draw, x_draw, y_draw):
    DISPLAY.blit(asset_name_draw, (x_draw, y_draw))

def check_border_collision(asset_to_move_x_pos, asset_to_move_y_pos, x, y, sprite_width, sprite_height):
    # Prevent the sprite from going out of bounds on all sides
    if asset_to_move_x_pos < 0:
        asset_to_move_x_pos = 0
    elif asset_to_move_x_pos > x - sprite_width:
        asset_to_move_x_pos = x - sprite_width

    if asset_to_move_y_pos < 0:
        asset_to_move_y_pos = 0
    elif asset_to_move_y_pos > y - sprite_height:
        asset_to_move_y_pos = y - sprite_height
    return asset_to_move_x_pos, asset_to_move_y_pos
def sprite_collision(player_x, player_y, enemy_x, enemy_y):
    if player_x < enemy_x + 50 and player_x + 50 > enemy_x and player_y < enemy_y + 50 and player_y + 50 > enemy_y:
        #Make this stop the sprites instead of teleportin the player
        previous_x, previous_y = player_x - 1, player_y - 1
        player_x = previous_x
        player_y = previous_y
        if player_x < previous_x:
            player_x = player_x + 1
        elif player_x > previous_x:
            player_x = player_x - 1
        if player_y < previous_y:
            player_y = player_y + 1
        elif player_y > previous_y:
            player_y = player_y - 1
        return True, player_x, player_y
    else:
        return False, player_x, player_y
#Use for debugging. examples below
def devmode(TF):
    if TF == True:
        print("Using devmode")
    else:
        print("Not using dev mode")
def random_number(lower_range, upper_range):
    randnum = random.randint(lower_range, upper_range)
    return randnum
def enemy_ai_movement(enemy_x, enemy_y, player_x, player_y, speed):
    """
    Moves the enemy towards the player.
    :param enemy_x: Enemy's current x position.
    :param enemy_y: Enemy's current y position.
    :param player_x: Player's current x position.
    :param player_y: Player's current y position.
    :param speed: Speed of the enemy.
    :return: Updated enemy_x, enemy_y positions.
    """
    if enemy_x < player_x:
        enemy_x += speed
    elif enemy_x > player_x:
        enemy_x -= speed

    if enemy_y < player_y:
        enemy_y += speed
    elif enemy_y > player_y:
        enemy_y -= speed

    return enemy_x, enemy_y
#test engine before merging
## collision is cooked
create_display(1080, 920)
set_display_title("test for my set of functions")
# Load the player sprite multiple sprite test
player_sprite = load_asset("enemy.png", "Assets")
enemy_sprite = load_asset("player.png", "Assets")
# Assume the sprite is 50px by 50px (you should adjust this based on your actual sprite size)
sprite_width, sprite_height = player_sprite.get_width(), player_sprite.get_height()
key = pygame.key.get_pressed()
# Ingitial position of the sprite
player_x, player_y = 250, 250
enemy_x, enemy_y = 250 + 50, 250 + 50
# Get the display size for collision checking
display_width, display_height = 1080, 920
#game loop stuff
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running= False
            print("process exited")
    #enable devmode
    devmode(True)
    # Update the sprite's position based on keyboard input
    player_x, player_y = add_default_movement(player_x, player_y)
    # Check for border collision
    player_x, player_y = check_border_collision(player_x, player_y, display_width, display_height, sprite_width, sprite_height)
    # Check for sprite collision
    collision_detected, player_x, player_y = sprite_collision(player_x, player_y, enemy_x, enemy_y)
    ##COMMENTING THIS LINE MAKE SOME STUPID THING HAPPEN???
    DISPLAY.fill(WHITE)  # White background
    # Draw the player and enemy sprites

    draw_sprite(player_sprite, player_x, player_y)
    draw_sprite(enemy_sprite, enemy_x, enemy_y)
    # Update the display
    pygame.display.update()
    if key[K_KP1] and devmode(True):
        player_x = player_x + 10
        player_y = player_y + 10
    random_number(1, 100)
    enemy_ai_movement(enemy_x, enemy_y, player_x, player_y, 1)
    draw_sprite(player_sprite, player_x, player_y)

#Quit pygame n stuff
pygame.quit()
sys.exit()
#end of test
