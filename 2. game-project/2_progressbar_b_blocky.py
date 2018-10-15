import pygame
import sys

pygame.init()
clock = pygame.time.Clock()

black = (0, 0, 0)
light_gray = (220, 220, 220)

padding = 10
width = 620
height = 70
block_width = 50
secs_to_fill = 5
fps = 60
cur_width = 0

screen = pygame.display.set_mode((width, height))
screen.fill(light_gray)
pygame.draw.rect(screen, black,
                 (padding, padding, block_width, height - padding * 2), 0)
pygame.display.update()
cur_blocks = 1

while True:
    for event in pygame.event.get():  # Exit game on X press
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    cur_width += (width - padding * 2) / (fps * secs_to_fill)
    if cur_width > (width - padding * 2):
        pygame.quit()
        sys.exit()

    if cur_width >= (cur_blocks + 1) * (block_width + padding):
        pygame.draw.rect(screen, black,
                         (cur_blocks * (block_width + padding) + padding,
                          padding,
                          block_width,
                          height - padding * 2
                          ), 0)
        cur_blocks += 1

    elapsed = clock.tick(fps)
    pygame.display.update()
