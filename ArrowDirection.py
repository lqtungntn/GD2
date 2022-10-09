import pygame
import os
import Global

class ArrowDirection(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.Position = [0, 0]
        self.Size = [15, 15]
        self.Angle = 0
        self.Image = pygame.transform.scale(pygame.image.load(os.path.join('Assets\\Game\\Player\\ArrowDirection.png')), (self.Size[0], self.Size[1]))

    def Draw(self):
        image_copy = pygame.transform.rotate(self.Image.copy(), self.Angle)
        pos = self.GetPosition()
        Global.WIN.blit(image_copy, (self.Position[0] + pos[0], self.Position[1] + pos[1]))

    def Input(self, event, team):
        if event.type == pygame.KEYDOWN:
            if team == 0:
                if event.key == pygame.K_s:
                    self.Angle = (self.Angle + 45) % 360
                elif event.key == pygame.K_w:
                    self.Angle = (self.Angle - 45 + 360) % 360
            else:
                if event.key == pygame.K_DOWN:
                    self.Angle = (self.Angle + 45) % 360
                elif event.key == pygame.K_UP:
                    self.Angle = (self.Angle - 45 + 360) % 360
    def GetVector(self):
        if self.Angle == 0:
            return [-1, 0]
        elif self.Angle == 315:
            return [-1, -1]
        elif self.Angle == 270:
            return [0, -1]
        elif self.Angle == 225:
            return [1, -1]
        elif self.Angle == 180:
            return [1, 0]
        elif self.Angle == 135:
            return [1, 1]
        elif self.Angle == 90:
            return [0, 1]
        elif self.Angle == 45:
            return [-1, 1]

    def GetPosition(self):
        if self.Angle == 0:
            return [0, 25]
        elif self.Angle == 45:
            return [0, 50]
        elif self.Angle == 90:
            return [25, 50]
        elif self.Angle == 135:
            return [50, 50]
        elif self.Angle == 180:
            return [50, 25]
        elif self.Angle == 225:
            return [50, 0]
        elif self.Angle == 270:
            return [25, 0]
        elif self.Angle == 315:
            return [0, 0]