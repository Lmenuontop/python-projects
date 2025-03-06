import pygame
import sys
import random
from pygame.locals import *

# Initialize Pygame
pygame.init()
# Define global variables
DISPLAY = None

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

def draw_sprite(asset_name_draw, x_draw, y_draw):
    DISPLAY.blit(asset_name_draw, (x_draw, y_draw))


# First run test
create_display(500, 500)
set_display_title("Pygame Window")

# Load the player sprite
player_sprite = load_asset("player.png", "Assets")

# Initial position of the sprite
player_x, player_y = 250, 250

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
    
    # Update the sprite's position based on keyboard input
    player_x, player_y = add_default_movement(player_x, player_y)
    
    # Fill the screen with a background color (optional)
    DISPLAY.fill((0, 0, 0))  # Black background
    
    # Draw the player sprite
    draw_sprite(player_sprite, player_x, player_y)
    
    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()
sys.exit()
