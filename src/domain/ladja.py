from dataclasses import dataclass
import pygame


@dataclass
class Ladja:
    x: int
    y: int
    dx: int
    dy: int

    def __post_init__(self):
        self.x = 0
        self.y = 0
        self.image = pygame.image.load("ladja.png")
        self.rect = self.image.get_rect()

    def draw(self, screen, x, y):
        screen.blit(self.image, (x, y))

    def premikanje(self):
        self.x += self.dx
        self.y += self.dy
