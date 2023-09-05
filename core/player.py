import pygame


class Player(pygame.Rect):
    def __init__(self):
        super(Player, self).__init__(20, 225, 20, 150)
        self.velocity = 5
        print("player class initiated!")
