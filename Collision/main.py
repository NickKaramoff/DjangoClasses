class Circle:
    def __init__(self, center_x, center_y, radius):
        self.center_x, self.center_y = center_x, center_y
        self.radius = radius


class Rectangle:
    def __init__(self, top_left_x, top_left_y, width, height):
        self.top_left_x, self.top_left_y = top_left_x, top_left_y
        self.width, self.height = width, height


class Line:
    def __init__(self, x1, y1, x2, y2):
        self.x1, self.y1 = x1, y1
        self.x2, self.y2 = x2, y2


BOARD_WID = 500
BOARD_HGT = 500
SIDEBAR_WID = 100
PADD = 15
WINDOW_WID = BOARD_WID + PADD * 2 + SIDEBAR_WID
WINDOW_HGT = BOARD_HGT + PADD * 2

BACKGROUND_COLOR = (240, 240, 240)
OBJECTS_COLOR = (85, 85, 85)
TEXT_COLOR = (0, 0, 0)

running = True

while running:
    pass
