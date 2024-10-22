import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up window
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption(" Car Animation")

# Function to draw an enhanced, detailed car
def draw_car(x, y):
    # Car body
    pygame.draw.rect(screen, (200, 0, 0), [x, y, 140, 50], 0, 15)  # Main body with rounded corners
    pygame.draw.polygon(screen, (200, 0, 0), [(x + 20, y), (x + 120, y), (x + 100, y - 25), (x + 40, y - 25)])  # Car roof
    
    # Windows
    pygame.draw.rect(screen, (0, 0, 0), [x + 25, y - 20, 35, 20])  # Front window
    pygame.draw.rect(screen, (0, 0, 0), [x + 70, y - 20, 30, 20])  # Rear window
    
    # Headlights and taillights
    pygame.draw.circle(screen, (255, 255, 0), (x + 135, y + 25), 8)  # Front headlight
    pygame.draw.circle(screen, (255, 0, 0), (x + 5, y + 25), 8)  # Rear taillight
    
    # Spoiler
    pygame.draw.polygon(screen, (100, 0, 0), [(x + 5, y), (x + 5, y - 10), (x + 35, y - 10), (x + 35, y)])  # Car spoiler

    # Wheels with rims
    pygame.draw.circle(screen, (0, 0, 0), (x + 35, y + 50), 20)  # Front wheel
    pygame.draw.circle(screen, (0, 0, 0), (x + 105, y + 50), 20)  # Rear wheel
    pygame.draw.circle(screen, (192, 192, 192), (x + 35, y + 50), 10)  # Front wheel hubcap
    pygame.draw.circle(screen, (192, 192, 192), (x + 105, y + 50), 10)  # Rear wheel hubcap

    # Rims inside wheels
    pygame.draw.circle(screen, (0, 0, 0), (x + 35, y + 50), 5)  # Front wheel rim
    pygame.draw.circle(screen, (0, 0, 0), (x + 105, y + 50), 5)  # Rear wheel rim

# Function to draw background elements (trees, buildings, road)
def draw_background_elements():
    pygame.draw.rect(screen, (50, 50, 50), [0, 450, screen_width, 150])  # Road
    pygame.draw.rect(screen, (0, 255, 0), [600, 300, 50, 100])  # Tree 1
    pygame.draw.rect(screen, (0, 255, 0), [200, 320, 40, 80])   # Tree 2
    pygame.draw.rect(screen, (128, 128, 128), [500, 250, 100, 200])  # Building 1
    pygame.draw.rect(screen, (128, 128, 128), [100, 200, 150, 250])  # Building 2

# Main function to run the animation
def main():
    clock = pygame.time.Clock()
    
    # Initial position and speed for the car
    car_x, car_y = 0, 400
    car_speed = 5  # Speed of the car
    
    # Main animation loop
    while True:
        screen.fill((135, 206, 235))  # Sky blue background
        
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        # Draw background elements
        draw_background_elements()
        
        # Draw the enhanced car design
        draw_car(car_x, car_y)
        
        # Move car
        car_x += car_speed
        
        # Reset car position when it moves off-screen
        if car_x > screen_width:
            car_x = -150  # Reset off the screen
        
        # Update display
        pygame.display.update()
        clock.tick(60)  # Limit frame rate to 60 FPS

if __name__ == "__main__":
    main()
