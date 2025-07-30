import pygame
import random
screen_width, screen_heigth= 500, 599
movement_speed=4
font_size=120
pygame.init()
background_image= pygame.transform.scale(pygame.image.load("bgo.jpg"),
("SCREEN_WIDTH, SCREEN_HEIGHT"))
font = pygame.font.SysFont("Times New Roman", "FONT_SIZE")
class Sprite(pygame.sprite.Sprite):
    def __init__(self,color,height,width):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(pygame.color('dodgerblue'))
        pygame.draw.rect(self.image, color, pygame.Rect(0, 0, width, height))
        self.rect = self.image.get_rect()
    def move(self, x_change, y_change):
        self.rect.x = max(
        min(self.rect.x + x_change, screen_width - self.rect.width), 0)
        self.rect.y = max(
        min(self.rect.y + y_change, screen_width - self.rect.height), 0)
screen=pygame.display.set_mode((screen_width,screen_heigth))
pygame.display.set_cation("sprite collision")
all_sprite=pygame.sprite.group()
Sprite1=Sprite(pygame.color('blue')30,30)
Sprite1.rect.x, Sprite1.rect.y=random.randint(
    0, screen_width - Sprite1.rect.width), random.randint(
        0, screen_heigth - Sprite1.rect.heigth)
all_sprite.add(Sprite1)
sprite2 = Sprite(pygame.Color('black'), 30, 30)
sprite2.rect.x, sprite2.rect.y = random.randint(
    0, screen_width - sprite2.rect.width), random.randint(
                0, screen_heigth - sprite2.rect.height)
all_sprite.add(sprite2)
running, won = True, False
clock = pygame.time.Clock()
while running:
      for event in pygame.event.get():
if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN
                                     and event.key == pygame.K_x):
      running = False

if not won:
    keys = pygame.key.get_pressed()
    x_change = (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * movement_speed
    y_change = (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * movement_speed
    Sprite1.move(x_change, y_change)

    if Sprite1.rect.colliderect(sprite2.rect):
      all_sprite.remove(sprite2)
      won = True
      screen.blit(background_image, (0, 0))
all_sprite.draw(screen)
 if won:
        win_text = font.render("You win!", True, pygame.Color('black'))
        screen.blit(win_text, ((screen_width - win_text.get_width()) // 2,
                           (screen_heigth - win_text.get_height()) // 2))
        pygame.display.flip()
        clock.tick(90)
        pygame.quit()