import pygame

class Settings:
    def __init__(self):
        self.window_width = 630
        self.window_height = 690
        self.rows = 9
        self.cols = 9
        self.white = (255, 255, 255)
        self.black = (0, 0, 0)
        self.red = (255, 0, 0)

    def redraw_window(self, window, board, time, tries):
        window.fill(self.white)

        font = pygame.font.SysFont("comicsans", 40)

        text = font.render(f"Time: {self.time(time)}", True, self.black)
        window.blit(text, (self.window_width - 160, self.window_width + 20))

        text = font.render("X "*tries, True, self.red)
        window.blit(text, (20, self.window_width + 20))

        board.draw_grid(window, self)

    def time(self, seconds):
        sec = seconds % 60
        min = seconds // 60
        hour = min // 60

        return f" {str(min)}:{str(sec)}"