# Example file showing a circle moving on screen
import pygame
from pygame import Surface

from core.scene import SceneManager, MenuScene


def show_fps(screen: Surface, clock: pygame.time.Clock, fps_font: pygame.font.Font, fps_bg: Surface):
    fps_text = str(int(clock.get_fps()))
    fps_surface = fps_font.render(fps_text, 1, pygame.Color("black"))
    # show the bg
    screen.blit(fps_bg, (0, 0))
    screen.blit(fps_surface, (0, 0))


def main():
    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption("Pong")
    clock = pygame.time.Clock()
    manager = SceneManager(MenuScene())
    running = True

    fps_bg = pygame.Surface((25, 25))
    fps_bg.fill((255, 255, 255))
    fps_font = pygame.font.SysFont("Arial", 20)

    while running:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False
        manager.scene.render(screen)
        show_fps(screen, clock, fps_font, fps_bg)
        manager.scene.handle_events(events)
        manager.scene.update(clock=clock, screen=screen)
        clock.tick(120)
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
