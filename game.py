import pygame
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

WIDTH = 20
HEIGHT = 20
MARGIN = 5


# Build grid array
grid = []
for row in range(10):
    grid.append([])
    for column in range(10):
        grid[row].append(0)

# grid[1][1] = 1
# grid[1][2] = 1
# grid[1][3] = 1
# grid[1][4] = 1
# grid[1][5] = 1
# grid[2][1] = 1
# grid[2][2] = 1
# grid[2][3] = 1
# grid[2][4] = 1
# grid[2][5] = 1
grid[5][5] = 1
grid[5][6] = 1
grid[6][5] = 1
grid[6][6] = 1

pygame.init()
 
# Set the width and height of the screen [width, height]
size = (255, 255)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Conway's game of life")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

def draw(row, column):
    # Drawing the grid
    for row in range(10):
        for column in range(10):
            color = WHITE
            neighbors = 0
            lower_row = row - 1
            left_column = column - 1
            upper_row = row + 1
            right_column = column + 1
            if lower_row > 0:
                if left_column > 0:
                    if grid[row-1][column-1] == 1:
                        neighbors += 1
                if right_column < 10:
                    if grid[row-1][column+1] == 1:
                        neighbors += 1
                if grid[row-1][column] == 1:
                    neighbors += 1
            if upper_row < 10:
                if left_column > 0:
                    if grid[row+1][column-1] == 1:
                        neighbors += 1
                if right_column < 10:
                    if grid[row+1][column+1] == 1:
                        neighbors += 1
                if grid[row+1][column] == 1:
                    neighbors += 1
            if left_column > 0:
                if grid[row][column-1] == 1:
                    neighbors += 1
            if right_column < 10:
                if grid[row][column+1] == 1:
                    neighbors += 1

            if neighbors >= 3:
                grid[row][column] = 1

            if grid[row][column] == 1:
                color = BLACK
                if neighbors < 2:
                    color = WHITE
                    grid[row][column] = 0

    pygame.draw.rect(screen, color, [(MARGIN + WIDTH) * column + MARGIN, (MARGIN + HEIGHT) * row + MARGIN, WIDTH, HEIGHT])
 
# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # User clicks the mouse. Get the position
            pos = pygame.mouse.get_pos()
            # Change the x/y screen coordinates to grid coordinates
            column = pos[0] // (WIDTH + MARGIN)
            row = pos[1] // (HEIGHT + MARGIN)
            # Set that location to one
            grid[row][column] = 1
            print("Click ", pos, "Grid coordinates: ", row, column)

    # Background
    screen.fill(BLACK)

    for row in range(10):
        for column in range(10):
            color = WHITE
            neighbors = 0
            lower_row = row - 1
            left_column = column - 1
            upper_row = row + 1
            right_column = column + 1
            if lower_row > 0:
                if left_column > 0:
                    if grid[row-1][column-1] == 1:
                        neighbors += 1
                if right_column < 10:
                    if grid[row-1][column+1] == 1:
                        neighbors += 1
                if grid[row-1][column] == 1:
                    neighbors += 1
            if upper_row < 10:
                if left_column > 0:
                    if grid[row+1][column-1] == 1:
                        neighbors += 1
                if right_column < 10:
                    if grid[row+1][column+1] == 1:
                        neighbors += 1
                if grid[row+1][column] == 1:
                    neighbors += 1
            if left_column > 0:
                if grid[row][column-1] == 1:
                    neighbors += 1
            if right_column < 10:
                if grid[row][column+1] == 1:
                    neighbors += 1

            if neighbors >= 3:
                grid[row][column] = 1
            if grid[row][column] == 1:
                color = BLACK
                if neighbors < 2:
                    color = WHITE
                    grid[row][column] = 0
            pygame.draw.rect(screen, color, [(MARGIN + WIDTH) * column + MARGIN, (MARGIN + HEIGHT) * row + MARGIN, WIDTH, HEIGHT])

    # Update screen
    pygame.display.flip()
    clock.tick(5)

pygame.quit()