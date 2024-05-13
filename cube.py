import pygame

class Cube:
    def __init__(self, value, row, col, width, height):
        self.value = value
        self.temp = 0
        self.row = row
        self.col = col
        self.width = width
        self.height = height
        self.selected = False

    def draw_cube(self, window):
        font = pygame.font.SysFont("comicsans", 40)

        size = self.width / 9
        x = self.col * size
        y = self.row * size

        if self.temp != 0 and self.value == 0:
            text = font.render(str(self.temp), True, (128, 128, 128))
            window.blit(text, (x+5, y+5))
        elif self.value != 0:
            text = font.render(str(self.value), True, (0, 0, 0))
            window.blit(text, (x + (size/2 - text.get_width()/2), y + (size/2 - text.get_height()/2)))

        if self.selected:
            pygame.draw.rect(window, (0, 153, 255), (x, y, size, size), 3)

    def set_value(self, value):
        self.value = value

    def set_temporary(self, value):
        self.temp = value