import pygame
import sys
from pygame.locals import *
from time import time, sleep
from settings import Settings
from board import Board

class SudokuGame:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.window = pygame.display.set_mode((self.settings.window_width, self.settings.window_height))
        pygame.display.set_caption("Sudoku")
        self.board = Board(self.settings)
        self.key = None
        self.start = time()
        self.tries = 0

    def run_game(self):
        while True:
            play_time = round(time() - self.start)
            self.check_events(play_time)
            self.settings.redraw_window(self.window, self.board, play_time, self.tries)
            pygame.display.update()

    def check_events(self, time):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                self.key_down_events(event)
            if event.type == MOUSEBUTTONDOWN:
                self.mouse_button_down_events(event)
        if self.board.selected and self.key is not None:
            self.board.sketch(self.key)

    def key_down_events(self, event):
        if event.key == K_1:
            self.key = 1
        elif event.key == K_2:
            self.key = 2
        elif event.key == K_3:
            self.key = 3
        elif event.key == K_4:
            self.key = 4
        elif event.key == K_5:
            self.key = 5
        elif event.key == K_6:
            self.key = 6
        elif event.key == K_7:
            self.key = 7
        elif event.key == K_8:
            self.key = 8
        elif event.key == K_9:
            self.key = 9
        elif event.key == K_DELETE:
            self.board.clear()
            self.key = None
        elif event.key == K_RETURN:
            self.return_key_event()
        elif event.key == K_SPACE:
            self.board.reset(self.settings)
            self.tries = 0
        elif event.key == K_CAPSLOCK:
            self.board.solve()

    def return_key_event(self):
        i, j = self.board.selected
        if self.board.cubes[i][j].temp != 0:
            if not self.board.place_num(self.board.cubes[i][j].temp):
                self.tries += 1
                if self.tries > 10:
                    self.lost()
                    sleep(1)
                    self.board.reset(self.settings)
                    self.tries = 0
            self.key = None
            if self.board.is_completed():
                self.won()
                sleep(1)
                self.display_time(time)
                sleep(1)

    def mouse_button_down_events(self, event):
        pos = pygame.mouse.get_pos()
        clicked = self.board.click(pos)
        if clicked:
            self.board.select(clicked[0], clicked[1])
            self.key = None

    def display_time(self, time):
        font = pygame.font.SysFont("agencyfb", 45)
        text = font.render(f"Time: {self.settings.time(time)}", True, self.settings.white, (255, 128, 0))
        text_rect = text.get_rect()
        text_rect.center = self.window.get_rect().center
        button = pygame.Rect((0, 0, 250, 100))
        button.center = self.window.get_rect().center
        self.window.fill((255, 128, 0), button)
        self.window.blit(text, text_rect)
        pygame.display.update()

    def won(self):
        self.display_result("You won!")

    def lost(self):
        self.display_result("You lost!")

    def display_result(self, message):
        font = pygame.font.SysFont("agencyfb", 45)
        text = font.render(message, True, self.settings.white, (255, 128, 0))
        text_rect = text.get_rect()
        text_rect.center = self.window.get_rect().center
        button = pygame.Rect((0, 0, 250, 100))
        button.center = self.window.get_rect().center
        self.window.fill((255, 128, 0), button)
        self.window.blit(text, text_rect)
        pygame.display.update()

if __name__ == '__main__':
    sdk = SudokuGame()
    sdk.run_game()
