# Import Necessary Libraries
import pygame
# Initialize required modules
pygame.init()
# Setup window geometry
screen = pygame.display.set_mode((400,500))
# Create a loop to run till the game is quit by the use
done = False
while not done:
# Clear the event queue
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    pygame.draw.rect(screen,(255,0,00),pygame.Rect(100,100,50,100),20)
    pygame.draw.circle(screen,(100,100,100),(300, 300), 50)
# Make the changes visible
    pygame.display.flip()