import pygame
import os
import Global

class ArrowPlayer(pygame.sprite.Sprite):
    def __init__(self, team):
        super().__init__()
        self.Position = [0, 0]
        self.Size = [15, 15]
        if team == 0:
            self.Image = pygame.transform.scale(pygame.image.load(os.path.join('Assets\\Game\\Player\\ArrowPlayer0.png')), (self.Size[0], self.Size[1]))
        else:
            self.Image = pygame.transform.scale(pygame.image.load(os.path.join('Assets\\Game\\Player\\ArrowPlayer1.png')), (self.Size[0], self.Size[1]))

    def Draw(self):
        Global.WIN.blit(self.Image, (self.Position[0] + 20, self.Position[1] - 20))