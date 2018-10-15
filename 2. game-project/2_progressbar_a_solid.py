import pygame
import sys

pygame.init()
clock = pygame.time.Clock()

black = (0, 0, 0)
light_gray = (220, 220, 220)

padding = 5
width = 540
height = 60
secs_to_fill = 5
fps = 60
cur_width = 0
end_reached = False

screen = pygame.display.set_mode((width, height))
screen.fill(light_gray)
pygame.draw.rect(screen, black,
                 (padding, padding, cur_width, height - padding * 2), 0)
pygame.display.update()

while True:
    for event in pygame.event.get():  # Exit game on X press
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if end_reached:
        pygame.quit()
        sys.exit()

    cur_width += (width - padding * 2) / (fps * secs_to_fill)
    if cur_width >= (width - padding * 2):
        end_reached = True
        cur_width = width - padding * 2

    screen.fill(light_gray)
    pygame.draw.rect(screen, black,
                     (padding, padding, cur_width, height - padding * 2), 0)
    elapsed = clock.tick(fps)
    pygame.display.update()
