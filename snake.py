import pygame, sys, random
from pygame.locals import *

pygame.init()
red = (255,0,0)
score = 0
# CREATING CANVAS
DISPLAY = pygame.display.set_mode((1080, 720))

# TITLE OF CANVAS
pygame.display.set_caption("Snake")

class Player(object):
    def __init__(self):
        self.rect = pygame.rect.Rect((60, 60, 30, 30))
        self.direction = "right"
        self.segments = [self.rect]
        self.initial_segments = 3
        for y in range(1, self.initial_segments):
            new_segment = pygame.rect.Rect(self.segments[-1].topleft, (30, 30))
            self.segments.append(new_segment)

    def handle_keys(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.direction = 'left'
        elif key[pygame.K_RIGHT]:
            self.direction = 'right'
        elif key[pygame.K_UP]:
            self.direction = 'up'
        elif key[pygame.K_DOWN]:
            self.direction = 'down'
        dist = 10  # Moved distance to align with segment size
        new_head = self.rect.copy()

        if self.direction == 'left':
            new_head = self.rect.move(-dist, 0)
        elif self.direction == 'right':
            new_head = self.rect.move(dist, 0)
        elif self.direction == 'up':
            new_head = self.rect.move(0, -dist)
        elif self.direction == 'down':
            new_head = self.rect.move(0, dist)

        self.segments = [new_head] + self.segments[:-1]
        self.rect = new_head

    def draw(self, surface):
        for segment in self.segments:
            pygame.draw.rect(surface, (0, 0, 128), segment)

    def check_bounds(self):
        display_width, display_height = DISPLAY.get_size()
        if self.rect.left < 0 or self.rect.right > display_width or self.rect.top < 0 or self.rect.bottom > display_height:
            self.rect.center = (display_width // 2, display_height // 2)
            self.segments = [self.rect]

    def print_coordinates(self):
        print("Top left:", self.rect.topleft)
        print("Top right:", self.rect.topright)
        print("Bottom left:", self.rect.bottomleft)
        print("Bottom right:", self.rect.bottomright)
        print("Center:", self.rect.center)

    def check_collision(self, food):
        if self.rect.colliderect(food.rect):
            return True
        return False

class Food():
    def __init__(self):
        self.rect = pygame.rect.Rect(random.randint(0, 1070), random.randint(0, 710), 15, 15)

    def draw(self, surface):
        pygame.draw.rect(surface, (255, 0, 0), self.rect)

food = Food()
player = Player()
WHITE = (255,255,255)
DISPLAY.fill(WHITE)
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    clock.tick(10)
    DISPLAY.fill(WHITE)
    player.draw(DISPLAY)
    player.handle_keys()
    player.print_coordinates()
    player.check_bounds()
    food.draw(DISPLAY)

    if player.check_collision(food):
        last_segment = player.segments[-1]
        if player.direction == 'left':
            new_segment = last_segment.move(30, 0)
        elif player.direction == 'right':
            new_segment = last_segment.move(-30, 0)
        elif player.direction == 'up':
            new_segment = last_segment.move(0, 30)
        elif player.direction == 'down':
            new_segment = last_segment.move(0, -30)
        player.segments.append(new_segment)
        food = Food() #makes new food
    pygame.display.update()
