import pygame


class Player(pygame.Rect):
    def __init__(self):
        super(Player, self).__init__(0, 0, 20, 150)
        self.x = 0
        self.y = 0
        self.width = 20
        self.height = 150
        print("player class initiated!")

    def move_by(self, x: int, y: int, max_x: int = 1280, max_y: int = 720) -> None:
        """
        Move the player by x and y, and clip its position inside the screen
        :param x: distance to move on the x-axis
        :param y: distance to move on the y-axis
        :param max_x: maximum x value (default: 1280)
        :param max_y: maximum y value (default: 720)
        :return: None
        """
        self.x += x
        self.y += y
        # Clip the player to the screen
        self.x = min(max_x - self.width, max(0, self.x))
        self.y = min(max_y - self.height, max(0, self.y))

    def render(self, screen: pygame.Surface):
        pygame.draw.rect(screen, (255, 255, 255), self)
