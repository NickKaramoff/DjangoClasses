import pygame
import sys

pygame.init()
clock = pygame.time.Clock()

start_color = (203, 40, 33)
end_color = (247, 242, 26)
light_gray = (220, 220, 220)

padding = 5
width = 540
height = 60
secs_to_fill = 5
fps = 30
cur_width = 0
cur_color = start_color
end_reached = False

screen = pygame.display.set_mode((width, height))
screen.fill(light_gray)
pygame.draw.rect(screen, cur_color,
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
    cur_color = (
        cur_color[0] + (end_color[0] - start_color[0]) / (fps * secs_to_fill),
        cur_color[1] + (end_color[1] - start_color[1]) / (fps * secs_to_fill),
        cur_color[2] + (end_color[2] - start_color[2]) / (fps * secs_to_fill)
    )

    if cur_width >= (width - padding * 2):
        end_reached = True
        cur_width = width - padding * 2

    screen.fill(light_gray)
    pygame.draw.rect(screen, cur_color,
                     (padding, padding, cur_width, height - padding * 2), 0)
    elapsed = clock.tick(fps)
    pygame.display.update()
