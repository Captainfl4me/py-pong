import pygame
from pygame import Surface
from core.player import Player


class Scene(object):
    def __init__(self):
        self.manager = None

    def render(self, screen: Surface):
        if self.manager is None:
            raise ValueError("Scene has no reference to SceneManager")
        raise NotImplementedError

    def update(self, clock: pygame.time.Clock = None, screen: Surface = None):
        if self.manager is None:
            raise ValueError("Scene has no reference to SceneManager")
        raise NotImplementedError

    def handle_events(self, events):
        if self.manager is None:
            raise ValueError("Scene has no reference to SceneManager")
        raise NotImplementedError


class MenuScene(Scene):
    def __init__(self):
        super(MenuScene, self).__init__()
        self.font = pygame.font.SysFont("Arial", 64)
        self.smallFont = pygame.font.SysFont("Arial", 18)

    def render(self, screen: Surface):
        screen_rect = screen.get_rect()
        screen.fill((0, 0, 0))
        text1 = self.font.render('Pong Rework', True, (255, 255, 255))
        text2 = self.smallFont.render('> press SPACE to start <', True, (255, 255, 255))
        screen.blit(text1, ((screen_rect.width - text1.get_rect().width)/2, 50))
        screen.blit(text2, ((screen_rect.width - text2.get_rect().width)/2, 250))

    def update(self, clock: pygame.time.Clock = None, screen: Surface = None):
        pass

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.manager.go_to(GameScene())


class GameScene(Scene):
    def __init__(self):
        super(GameScene, self).__init__()
        self.font = pygame.font.SysFont("Arial", 18)
        self.player1 = Player()

    def render(self, screen: Surface):
        screen.fill((0, 0, 0))
        self.player1.render(screen)

    def update(self, clock: pygame.time.Clock = None, screen: Surface = None):
        # Check for key presses
        keys = pygame.key.get_pressed()
        if keys[pygame.K_z]:
            self.player1.move_by(0, -clock.get_time(), screen.get_rect().width, screen.get_rect().height)
        if keys[pygame.K_s]:
            self.player1.move_by(0, clock.get_time(), screen.get_rect().width, screen.get_rect().height)

    def handle_events(self, events):
        pass


class SceneManager(object):
    def __init__(self, default_scene: Scene):
        self.scene = None
        self.default_scene = default_scene
        self.go_to(self.default_scene)

    def go_to(self, scene: Scene):
        self.scene = scene
        self.scene.manager = self
