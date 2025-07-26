import pygame
def main():
    pygame.init()
    screen_width,screen_heigth= 600, 500
    screen=pygame.display.set_mode((screen_width,screen_heigth))
    pygame.display.set_caption('color changing sprite')
    colors={
        'red': pygame.Color('red'),
        'orange': pygame.Color('orange'),
        'purple': pygame.Color('purple'),
        'green': pygame.Color('green'),
        'yellow':pygame.Color('yellow')
    }
    current_color = colors['yellow']
    x, y= 180, 120
    sprite_width, sprite_height = 75, 80
    clock = pygame.time.Clock()
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT]: x -= 3
        if pressed[pygame.K_RIGHT]: x += 3
        if pressed[pygame.K_UP]: y -= 3
        if pressed[pygame.K_DOWN]: y += 3
        x = min(max(0, x), screen_width - sprite_width)
        y = min(max(0, y), sprite_height - sprite_height)
        if x == 0: current_color = colors['orange']
        elif x == screen_width - sprite_width: current_color = colors['yellow']
        elif y == sprite_height - sprite_height:
            current_color = colors['green']
        else:
            current_color = colors['white']
            screen.fill((0, 0, 0))
        pygame.draw.rect(screen, current_color,(x, y, sprite_width, sprite_height))
        pygame.display.flip()
        clock.tick(90)
        pygame.quit()
if __name__ == "__main__":
    main()