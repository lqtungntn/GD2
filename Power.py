import pygame
import os
import Global


class Power(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.Size = [800, 15]
        self.Up = 0
        self.Energy = 0.0
        self.Begin = False
        self.Image = pygame.transform.scale(pygame.image.load(os.path.join('Assets\\Game\\Player\\Power.png')), (self.Size[0], self.Size[1]))

    def Draw(self):
        self.Energy = min(self.Energy + self.Up, 20.0)
        Global.WIN.blit(self.Image, (100, 500), (0, 0, 40 * self.Energy, 15))

    def Input(self, event, team):
        if self.Begin:
            if team == 0:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        self.Up = 0.5
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_c:
                        self.Up = 0.0
                        self.Begin = False
            else:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_l:
                        self.Up = 0.5
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_l:
                        self.Up = 0.0
                        self.Begin = False
