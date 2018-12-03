from math import sqrt

import pygame


class Shape:
    movement_speed = 10

    def __init__(self, x, y):
        self.x, self.y = x, y

    def move_up(self):
        self.y -= self.movement_speed

    def move_down(self):
        self.y += self.movement_speed

    def move_left(self):
        self.x -= self.movement_speed

    def move_right(self):
        self.x += self.movement_speed


class Circle(Shape):
    def __init__(self, center_x, center_y, radius):
        super().__init__(center_x, center_y)
        self.radius = radius


class Rectangle(Shape):
    def __init__(self, top_left_x, top_left_y, width, height):
        super().__init__(top_left_x, top_left_y)
        self.width, self.height = width, height


class Line(Shape):
    def __init__(self, x1, y1, x2, y2):
        super().__init__(x1, y1)
        self.x2, self.y2 = x2, y2


def check_collision(rectangle, circle):
    rectangle_box = (rectangle.x,
                     rectangle.y,
                     rectangle.x + rectangle.width,
                     rectangle.y + rectangle.height)
    circle_box = (circle.x - circle.radius,
                  circle.y - circle.radius,
                  circle.x + circle.radius,
                  circle.y + circle.radius)

    if rectangle_box[0] > circle_box[2] \
            or rectangle_box[1] > circle_box[3] \
            or rectangle_box[2] < circle_box[0] \
            or rectangle_box[3] < circle_box[1]:
        return False

    for x in (rectangle_box[0], rectangle_box[2]):
        for y in (rectangle_box[1], rectangle_box[3]):
            if sqrt((x - circle.x) ^ 2 + (y - circle.y) ^ 2) <= circle.radius:
                print(sqrt((x - circle.x) ^ 2 + (y - circle.y) ^ 2), circle.radius)
                return True


# Screen parameters
BOARD_WID = 500
BOARD_HGT = 500
SIDEBAR_WID = 200
PADD = 15
WINDOW_WID = BOARD_WID + PADD * 2 + SIDEBAR_WID
WINDOW_HGT = BOARD_HGT + PADD * 2
WINDOW_CAPTION = "Collision"
FPS = 60

# Board borders
TOP_Y = PADD
BOT_Y = PADD + BOARD_HGT
LFT_X = PADD
RGT_X = PADD + BOARD_WID

# Colors
BOARD_COLOR = (240, 240, 240)
BACKGROUND_COLOR = (255, 255, 255)
OBJECTS_COLOR = (85, 85, 85)
TEXT_COLOR = (0, 0, 0)

pygame.init()
FONT = pygame.font.Font(None, 24)

screen = pygame.display.set_mode((WINDOW_WID, WINDOW_HGT))
pygame.display.set_caption(WINDOW_CAPTION)
CLOCK = pygame.time.Clock()

running = True
collision = False

objects = [Circle(100, 100, 50), Rectangle(200, 200, 100, 100)]

selected_index = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

            elif event.key == pygame.K_1:
                selected_index = 0
            elif event.key == pygame.K_2:
                selected_index = 1

            elif event.key == pygame.K_UP:
                objects[selected_index].move_up()
            elif event.key == pygame.K_DOWN:
                objects[selected_index].move_down()
            elif event.key == pygame.K_LEFT:
                objects[selected_index].move_left()
            elif event.key == pygame.K_RIGHT:
                objects[selected_index].move_right()

    screen.fill(BACKGROUND_COLOR)
    pygame.draw.rect(screen, BOARD_COLOR, [PADD, PADD, BOARD_WID, BOARD_HGT], 0)

    for obj in objects:
        if type(obj) is Circle:
            pygame.draw.circle(screen, OBJECTS_COLOR, (obj.x, obj.y), obj.radius, 0)
        elif type(obj) is Rectangle:
            pygame.draw.rect(screen, OBJECTS_COLOR, [obj.x, obj.y, obj.width, obj.height], 0)

    collision = check_collision(objects[1], objects[0])

    instr_text = FONT.render('Selected object %d' % (selected_index + 1), 1, TEXT_COLOR)
    instr_text_pos = instr_text.get_rect()
    instr_text_pos.centerx = BOARD_WID + PADD * 2 + SIDEBAR_WID / 2
    instr_text_pos.centery = WINDOW_HGT - PADD - instr_text.get_height() / 2
    screen.blit(instr_text, instr_text_pos)

    coll_text = FONT.render('COLLIDING!' if collision else 'Not colliding', 1, TEXT_COLOR)
    coll_text_pos = coll_text.get_rect()
    coll_text_pos.centerx = BOARD_WID + PADD * 2 + SIDEBAR_WID / 2
    coll_text_pos.centery = WINDOW_HGT / 2
    screen.blit(coll_text, coll_text_pos)

    pygame.display.flip()
    CLOCK.tick(FPS)
