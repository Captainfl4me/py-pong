import pygame
from pygame import Surface


class Scene(object):
    def __init__(self):
        self.manager = None

    def render(self, screen: Surface):
        if self.manager is None:
            raise ValueError("Scene has no reference to SceneManager")
        raise NotImplementedError

    def update(self):
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
        self.font = pygame.font.SysFont("Arial", 18)
        self.smallFont = pygame.font.SysFont("Arial", 32)

    def render(self, screen: Surface):
        screen.fill((0, 0, 0))
        text1 = self.font.render('Pong Rework', True, (255, 255, 255))
        text2 = self.smallFont.render('> press SPACE to start <', True, (255, 255, 255))
        screen.blit(text1, (200, 50))
        screen.blit(text2, (200, 350))

    def update(self):
        pass

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    self.manager.go_to(GameScene())


class GameScene(Scene):
    def __init__(self):
        super(GameScene, self).__init__()
        self.font = pygame.font.SysFont("Arial", 18)
        self.smallFont = pygame.font.SysFont("Arial", 32)

    def render(self, screen: Surface):
        screen.fill((255, 0, 0))

    def update(self):
        pass

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
