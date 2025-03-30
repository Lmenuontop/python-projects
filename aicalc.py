import pygame
import sys
from pygame import *
pygame.init()

pygame.display.set_caption("WIP Visual Calculator")
white = (255, 255, 255)
DISPLAY = pygame.display.set_mode((400, 250))  # Increased width to make space for result

# Load images for buttons
add = pygame.image.load('Assets/add.png')
subtract = pygame.image.load('Assets/subtract.png')
one = pygame.image.load('Assets/one.png')
two = pygame.image.load('Assets/two.png')
three = pygame.image.load('Assets/three.png')
four = pygame.image.load('Assets/four.png')
five = pygame.image.load('Assets/five.png')
six = pygame.image.load('Assets/six.png')
seven = pygame.image.load('Assets/seven.png')
eight = pygame.image.load('Assets/eight.png')
nine = pygame.image.load('Assets/nine.png')
zero = pygame.image.load('Assets/zero.png')
equal = pygame.image.load('Assets/equal.png')
divide = None #no divide button yet
button_spacing = 50

# Define the positions and sizes of buttons (x, y, width, height)
buttons = [
    (one, 0, 0), (two, button_spacing, 0), (three, button_spacing * 2, 0),
    (four, 0, button_spacing), (five, button_spacing, button_spacing), (six, button_spacing * 2, button_spacing),
    (seven, 0, button_spacing * 2), (eight, button_spacing, button_spacing * 2), (nine, button_spacing * 2, button_spacing * 2),
    (zero, button_spacing, button_spacing * 3), (add, button_spacing, button_spacing * 4),
    (subtract, button_spacing + 50, button_spacing * 4), (equal, button_spacing - 50, button_spacing * 4)
]

# Variables to store the input
input_str = ""  # This will store the current input string
current_operation = None  # Store the current operation (+ or -)
first_value = None  # Store the first value before the operation
# s1 = int(input("addition idk: "))
# s2 = int(input("addition v2: "))
# Function to check if a mouse click is inside a button
def button_clicked(x, y, button_rect):
    return button_rect.collidepoint(x, y)

# Function to perform the calculation
def calculate_result():
    global input_str, current_operation, first_value
    try:
        if current_operation == '+':
            result = first_value + float(input_str)
        elif current_operation == '-':
            result = first_value - float(input_str)
        else:
            result = float(input_str)
        return result
    except Exception as e:
        print(f"Error: {e}")
        return "error"
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == MOUSEBUTTONDOWN:  # Check for mouse click
            mouse_x, mouse_y = event.pos  # Get mouse position

            # Check each button for a click
            for button_image, x, y in buttons:
                button_rect = pygame.Rect(x, y, button_image.get_width(), button_image.get_height())
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
                            first_value = float(input_str) if input_str else 0
                        current_operation = "+"
                        input_str = ""  # Clear input for the next number
                    elif button_image == subtract:
                        if first_value is None:
                            first_value = float(input_str) if input_str else 0
                        current_operation = "-"
                        input_str = ""  # Clear input for the next number

                    # Handle equal button
                    elif button_image == equal:
                        if first_value is not None and input_str != "":
                            result = calculate_result()
                            input_str = str(result)
                            first_value = None  # Reset the first value after calculation
                            current_operation = None  # Reset operation
if s1 > 0 and s2 > 0:
    print(s1 + s2)
    # Draw the calculator interface
    DISPLAY.fill(white)  # Clear screen

    # Draw the input/output on the left part of the screen
    font = pygame.font.Font(None, 36)
    text_surface = font.render(input_str, True, (0, 0, 0))
    DISPLAY.blit(text_surface, (10, 10))  # Display the current input/output

    # Draw the result on the right side of the screen
    if input_str != "":
        result_surface = font.render(input_str, True, (0, 0, 0))  # This is the result text
    else:
        result_surface = font.render("0", True, (0, 0, 0))  # Display 0 when nothing is entered
    DISPLAY.blit(result_surface, (300, 10))  # Positioning result on the right side of the screen

    # Blit images to the screen
    for button_image, x, y in buttons:
        DISPLAY.blit(button_image, (x, y))
    pygame.display.update()  # Update the display
