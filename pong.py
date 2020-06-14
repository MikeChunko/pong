# Implementation of Pong in pygame
import pygame as pyg
import random


class Pong:
    def __init__(self, screen_x=300, screen_y=300):
        pyg.init()
        pyg.font.init()
        self.screen_x, self.screen_y = screen_x, screen_y
        self.screen = pyg.display.set_mode((self.screen_x, self.screen_y))
        self.white = (255, 255, 255)
        self.size_x = self.size_y = 10  # "Pixel" size
        pyg.display.update()
        pyg.display.set_caption("Pong")
        self.clock = pyg.time.Clock()

        # _1 is for the player, _2 is for the computer
        self.score_1 = self.score_2 = 0
        self.paddle_1 = self.paddle_2 = screen_y // 2 - (2 * self.size_y)
        self.paddle_length = 5
        self.ball_x, self.ball_y = screen_x // 2, screen_y // 2
        self.gameover = False

    # TODO
    def display(self):
        self.screen.fill((0, 0, 0))

        pyg.draw.rect(self.screen, self.white, [self.ball_x, self.ball_y, self.size_x, self.size_y])

        for i in range (0, self.paddle_length * self.size_x, self.size_x):  # Paddles
            pyg.draw.rect(self.screen, self.white, [0, self.paddle_1 + i, self.size_x, self.size_y])
            pyg.draw.rect(self.screen, self.white, [self.screen_x - self.size_x, self.paddle_2 + i, self.size_x, self.size_y])

        for i in range(0, self.screen_x, self.size_x):  # Border
            pyg.draw.rect(self.screen, self.white, [i, 0, self.size_x, self.size_y])
            pyg.draw.rect(self.screen, self.white, [i, self.screen_y - self.size_y, self.size_x, self.size_y])

    def process_keyboard_input(self):
        for event in pyg.event.get():
            if event.type == pyg.QUIT:
                pyg.quit()
                quit()
            if event.type == pyg.KEYDOWN:  # Movement keys
                if event.key == pyg.K_UP or event.key == pyg.K_w:
                    self.get_input(0)
                elif event.key == pyg.K_DOWN or event.key == pyg.K_s:
                    self.get_input(1)

    # TODO
    def get_input(self, input):
        if input == 0:
            pass
        elif input == 1:
            pass

    def step(self, tick=15):
        self.process_keyboard_input()

        self.display()  # Draw

        pyg.display.update()
        self.clock.tick(tick)


if __name__ == "__main__":
    tick = 15
    while True:
        game = Pong()
        while not game.gameover:
            game.step(tick=tick)

        # Game over state
        # TODO - gameover text
        sentinel = True
        while sentinel:
            for event in pyg.event.get():
                if event.type == pyg.QUIT:
                    pyg.quit()
                    quit()
                if event.type == pyg.KEYDOWN and event.key == pyg.K_r:
                    sentinel = False

            game.display()

            pyg.display.update()
            game.clock.tick(tick)
