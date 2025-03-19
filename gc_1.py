import pygame
import sys
from pygame.locals import *
pygame.init()
button_image = ""
pygame.display.set_caption("WIP visual calculator")
white = (255, 255, 255)
DISPLAY = pygame.display.set_mode((250, 250))
add = pygame.image.load("Assets/add.png")
subtract = pygame.image.load("Assets/subtract.png")
one = pygame.image.load("Assets/one.png")
two = pygame.image.load("Assets/two.png")
three = pygame.image.load("Assets/three.png")
four = pygame.image.load("Assets/four.png")
five = pygame.image.load("Assets/five.png")
six = pygame.image.load("Assets/six.png")
seven = pygame.image.load("Assets/seven.png")
eight = pygame.image.load("Assets/eight.png")
nine = pygame.image.load("Assets/nine.png")
zero = pygame.image.load("Assets/zero.png")
equal = pygame.image.load("Assets/equal.png")
multiply = pygame.image.load("Assets/multiply.png")
divide = pygame.image.load("Assets/divide.png")
first_str = "."
second_str = "."
mouse_y = 0
mouse_x = 0

button_spacing = 50
buttons = [
    (one, 0, 0),
    (two, button_spacing, 0),
    (three, button_spacing * 2, 0),
    (four, 0, button_spacing),
    (five, button_spacing, button_spacing),
    (six, button_spacing * 2, button_spacing),
    (seven, 0, button_spacing * 2),
    (eight, button_spacing, button_spacing * 2),
    (nine, button_spacing * 2, button_spacing * 2),
    (zero, button_spacing, button_spacing * 3),
    (add, button_spacing, button_spacing * 4),
    (subtract, button_spacing + 50, button_spacing * 4),
    (equal, button_spacing - 50, button_spacing * 4),
    (divide, button_spacing - 50, button_spacing * 3),
    (multiply, button_spacing + 50, button_spacing * 3),
]

input_str = ""
first_value = ""
second_value = ""


def button_clicked(x, y, button_rect):
    return button_rect.collidepoint(x, y)

print("tomato")
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            print("Bye :(")
        if event.type == MOUSEBUTTONDOWN:  # Check for mouse click
            mouse_x, mouse_y = event.pos  # Get mouse position

            # Check each button for a click
            for button_image, x, y in buttons:
                button_rect = pygame.Rect(
                    x, y, button_image.get_width(), button_image.get_height()
                )
                if button_clicked(mouse_x, mouse_y, button_rect):
                    print(f"Button clicked at position ({x}, {y})")

                    # Handle number buttons
                    if button_image == one:
                        input_str += "1"
                    elif button_image == two:
                        input_str += "2"
                    elif button_image == three:
                        input_str += "3"
                    elif button_image == four:
                        input_str += "4"
                    elif button_image == five:
                        input_str += "5"
                    elif button_image == six:
                        input_str += "6"
                    elif button_image == seven:
                        input_str += "7"
                    elif button_image == eight:
                        input_str += "8"
                    elif button_image == nine:
                        input_str += "9"
                    elif button_image == zero:
                        input_str += "0"

                    # Handle operators
                    elif button_image == add:
                        if first_value is None:
                            first_value = float(input_str)
                        current_operation = "+"
                        input_str = ""  # Clear input for the next number
                    elif button_image == subtract:
                        if first_value is None:
                            first_value = float("input_str")
                        current_operation = "-"
                        print(current_operation)
                    elif button_image == multiply:
                        if first_value is None:
                            first_value = float(input_str)
                        current_operation = "*"
                    elif button_image == divide:
                        if first_value is None:
                            first_value = float(input_str)
                        current_operation = "/"

                    if button_image == one:
                        first_str = ""
                        first_str = "1"
                    elif button_image == two:
                        first_str = ""
                        first_str = "2"
                    elif button_image == three:
                        first_str = ""
                        first_str = "3"
                    elif button_image == four:
                        first_str = ""
                        first_str = "4"
                    elif button_image == five:
                        first_str = ""
                        first_str = "5"
                    elif button_image == six:
                        first_str = ""
                        first_str = "6"
                    elif button_image == seven:
                        first_str = ""
                        first_str = "7"
                    elif button_image == eight:
                        first_str = ""
                        first_str = "8"
                    elif button_image == nine:
                        first_str = ""
                        first_str = "9"
                    elif button_image == zero:
                        first_str = ""
                        first_str = "0"
                    if button_image == one:
                        second_str= ""
                        second_str = "1"
                    elif button_image == two:
                        second_str = ""
                        second_str = "2"
                    elif button_image == three:
                        second_str = ""
                        second_str = "3"
                    elif button_image == four:
                        second_str = ""
                        second_str = "4"
                    elif button_image == five:
                        second_str = ""
                        second_str = "5"
                    elif button_image == six:
                        second_str = ""
                        second_str = "6"
                    elif button_image == seven:
                        second_str = ""
                        second_str = "7"
                    elif button_image == eight:
                        second_str = ""
                        second_str = "8"
                    elif button_image == nine:
                        second_str = ""
                        second_str = "9"
                    elif button_image == zero:
                        second_str = ""
                        second_str = "0"

                    print("first: ",first_str, " second: ",second_str)
                    ##You could concatonate firststr, operator and second str and be faster instead of typing every possibility
                    if first_str == "1" and second_str = "1" and current_operation = "add":
                
# Blit images to screen with reduced spacing chatgpt comment
    DISPLAY.fill(white)
    DISPLAY.blit(one, (0, 0))
    DISPLAY.blit(two, (button_spacing, 0))
    DISPLAY.blit(three, (button_spacing * 2, 0))
    DISPLAY.blit(four, (0, button_spacing))
    DISPLAY.blit(five, (button_spacing, button_spacing))
    DISPLAY.blit(six, (button_spacing * 2, button_spacing))
    DISPLAY.blit(seven, (0, button_spacing * 2))
    DISPLAY.blit(eight, (button_spacing, button_spacing * 2))
    DISPLAY.blit(nine, (button_spacing * 2, button_spacing * 2))
    DISPLAY.blit(zero, (button_spacing, button_spacing * 3))
    DISPLAY.blit(add, (button_spacing, button_spacing * 4))
    DISPLAY.blit(subtract, (button_spacing + 50, button_spacing * 4))
    DISPLAY.blit(equal, (button_spacing - 50, button_spacing * 4))
    DISPLAY.blit(multiply, (button_spacing - 50, button_spacing * 3))
    DISPLAY.blit(divide, (button_spacing + 50, button_spacing * 3))
    pygame.display.update()  # Update the display to show the images
    pygame.display.flip()
