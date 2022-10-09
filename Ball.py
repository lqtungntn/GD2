import pygame
import os
import Global

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.Size = [20, 20]
        self.DefaultPos = [Global.WIDTH // 2 - self.Size[0] // 2, Global.HEIGHT // 2 - self.Size[1] // 2]
        self.Position = []
        self.BallImage = pygame.transform.scale(pygame.image.load(os.path.join('Assets\\Game\\Player\\Ball.png')), (self.Size[0], self.Size[1]))
        self.Acceleration = 0.1
        self.Speed = 0.0
        self.VectorUnit = [1, 1]
        self.State = 1 # 0 : dribble, 1: death ball
        self.PlayerFaceDir = 0
        self.Player = -1
        self.Team = 1 # 1: player 1, 2: player 2
        self.Hcn = Global.WIN.blit(self.BallImage, (0, 0))

    def Draw(self):
        if self.State == 0:
            if self.PlayerFaceDir == 1:
                self.Hcn = Global.WIN.blit(self.BallImage, (self.Position[0] + 30, self.Position[1] + 30))
            else:
                self.Hcn = Global.WIN.blit(self.BallImage, (self.Position[0], self.Position[1] + 30))
        elif self.State == 1:
            self.CheckCollider()
            self.Position[0] += self.Speed * self.VectorUnit[0]
            self.Position[1] += self.Speed * self.VectorUnit[1]
            self.Speed = max(0.0, self.Speed - self.Acceleration)
            self.Hcn = Global.WIN.blit(self.BallImage, (self.Position[0], self.Position[1]))

    def CheckCollider(self):
        if self.Position[0] - self.Size[0] / 2 < 0:
            self.VectorUnit[0] = -self.VectorUnit[0]
        if self.Position[1] - self.Size[1] / 2 < 0:
            self.VectorUnit[1] = -self.VectorUnit[1]
        if self.Position[0] + self.Size[0] / 2 > Global.WIDTH:
            self.VectorUnit[0] = -self.VectorUnit[0]
        if self.Position[1] + self.Size[1] / 2 > Global.HEIGHT:
            self.VectorUnit[1] = -self.VectorUnit[1]

    def Reset(self):
        self.Position = self.DefaultPos.copy()
        self.Speed = 0
        self.State = 1
        self.Player = -1

    def GoDir(self, speed, vector):
        self.Speed = speed
        self.VectorUnit = vector
        self.State = 1

    def CollidePlayer(self, img):
        Tolerance = self.Speed
        if abs(img.Hcn.top - self.Hcn.bottom) < Tolerance:
            self.VectorUnit[1] = -self.VectorUnit[1]
        if abs(img.Hcn.bottom - self.Hcn.top) < Tolerance:
            self.VectorUnit[1] = -self.VectorUnit[1]
        if abs(img.Hcn.left - self.Hcn.right) < Tolerance:
            self.VectorUnit[0] = -self.VectorUnit[0]
        if abs(img.Hcn.right - self.Hcn.left) < Tolerance:
            self.VectorUnit[0] = -self.VectorUnit[0]


