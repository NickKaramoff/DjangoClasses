import pygame
import sys

pygame.init()
clock = pygame.time.Clock()

black = (0, 0, 0)
light_gray = (220, 220, 220)

width = 500
height = 500
radius = 100
secs_to_fill = 5
fps = 30

rect_x = (width - (radius * 2)) / 2
rect_y = (height - (radius * 2)) / 2
pi = 3.141592653589793238462643383279
start_angle = pi / 2
cur_angle = start_angle
end_angle = - 3 * pi / 2
end_reached = False


def draw_arc(start, end):
    pygame.draw.arc(screen, black, (rect_x, rect_y, radius * 2, radius * 2),
                    start,
                    end, 10)


screen = pygame.display.set_mode((width, height))
screen.fill(light_gray)
draw_arc(cur_angle, end_angle)

pygame.display.update()
while True:
    for event in pygame.event.get():  # Exit game on X press
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if end_reached:
        pygame.quit()
        sys.exit()

    cur_angle += (end_angle - start_angle) / (fps * secs_to_fill)
    if cur_angle <= end_angle:
        pygame.quit()
        sys.exit()

    draw_arc(cur_angle, end_angle)
    elapsed = clock.tick(fps)
    pygame.display.update()
