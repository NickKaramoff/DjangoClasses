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

screen = pygame.display.set_mode((WINDOW_WID, WINDOW_HGT))
pygame.display.set_caption(WINDOW_CAPTION)
CLOCK = pygame.time.Clock()

running = True

objects = [Circle(100, 100, 50), Rectangle(400, 400, 100, 100)]

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

    pygame.display.flip()
    CLOCK.tick(FPS)
