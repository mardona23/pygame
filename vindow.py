import pygame
pygame.init()
screen = pygame.display.set_mode((400,500))
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    pygame.draw.rect(screen,(255,0,00),pygame.Rect(100,250,50,100),50)
    pygame.draw.circle(screen,(100,200,250),(300, 300), 25)
    pygame.display.flip()