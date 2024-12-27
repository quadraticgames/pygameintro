import pygame  # type: ignore

# Initialize Pygame library
pygame.init()

# Set up the display window dimensions (width and height)
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))  # Creates the display surface/window
pygame.display.set_caption("Move a Character Example")  # Sets the window title

# Define the character's properties
x, y = 400, 300  # Starting position of the character (center of the screen)
width, height = 50, 50  # Size of the character (a 50x50 rectangle)
color = (255, 0, 0)  # Color of the character (Red, in RGB)
speed = 5  # How many pixels the character moves per key press

# Initialize the game loop variables
running = True  # This flag controls the game loop, set to False when the user quits the game
clock = pygame.time.Clock()  # Creates a clock object to control the frame rate of the game

# Start of the game loop
while running:
    # Event handling: Check for events like key presses or closing the window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # If the window close button is clicked
            running = False  # Stop the game loop, which will end the game

    # Handle key presses for character movement
    keys = pygame.key.get_pressed()  # Returns a list of boolean values for all keys
    if keys[pygame.K_LEFT]:  # If the left arrow key is pressed
        x -= speed  # Move the character left by decreasing its x-coordinate
    if keys[pygame.K_RIGHT]:  # If the right arrow key is pressed
        x += speed  # Move the character right by increasing its x-coordinate
    if keys[pygame.K_UP]:  # If the up arrow key is pressed
        y -= speed  # Move the character up by decreasing its y-coordinate
    if keys[pygame.K_DOWN]:  # If the down arrow key is pressed
        y += speed  # Move the character down by increasing its y-coordinate

    # Prevent the character from moving off-screen by clamping its position
    x = max(0, min(screen_width - width, x))  # x-coordinate must stay within the screen's width
    y = max(0, min(screen_height - height, y))  # y-coordinate must stay within the screen's height

    # Fill the screen with a black background before drawing the character
    screen.fill((0, 0, 0))  # RGB value (0, 0, 0) represents black

    # Draw the character (a red rectangle) at the new position
    pygame.draw.rect(screen, color, (x, y, width, height))  # Draw a rectangle at (x, y)

    # Update the display to reflect the changes (e.g., moving the rectangle)
    pygame.display.update()

    # Control the frame rate to ensure the game runs smoothly (30 frames per second)
    clock.tick(30)

# Quit the Pygame library and close the window when the game loop is finished
pygame.quit()