import pygame
import sys

pygame.init()
clock = pygame.time.Clock()

black = (0, 0, 0)
white = (255, 255, 255)
light_gray = (220, 220, 220)
states = [
    [
        (100, 50),
        (250, 50),
        (250, 100),
        (180, 170),
        (180, 180),
        (250, 250),
        (250, 300),
        (100, 300),
        (100, 250),
        (170, 180),
        (170, 170),
        (100, 100),
        (100, 50)
    ],
    [
        (215, 30),
        (320, 135),
        (280, 175),
        (180, 175),
        (175, 180),
        (175, 280),
        (135, 320),
        (30, 215),
        (70, 175),
        (170, 175),
        (175, 170),
        (175, 70),
        (215, 30)
    ],
    [
        (50, 100),
        (100, 100),
        (170, 170),
        (180, 170),
        (250, 100),
        (300, 100),
        (300, 250),
        (250, 250),
        (180, 180),
        (170, 180),
        (100, 250),
        (50, 250),
        (50, 100)
    ],
    [
        (135, 30),
        (30, 135),
        (70, 175),
        (170, 175),
        (175, 180),
        (175, 280),
        (215, 320),
        (320, 215),
        (280, 175),
        (180, 175),
        (175, 170),
        (175, 70),
        (135, 30)
    ]
]

cur_state = 0
line_width = 3

screen = pygame.display.set_mode((350, 350))
screen.fill(light_gray)
pygame.draw.lines(screen, black, False, states[cur_state], line_width)
pygame.display.update()


while True:
    for event in pygame.event.get():  # Exit game on X press
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    cur_state += 1
    if cur_state >= len(states):
        cur_state = 0

    screen.fill(light_gray)
    pygame.draw.lines(screen, black, False, states[cur_state], line_width)
    elapsed = clock.tick(5)
    pygame.display.update()
