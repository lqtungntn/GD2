import pygame
import os
import Global

class Goal(pygame.sprite.Sprite):
    def __init__(self, team, cx, cy):
        super().__init__()
        self.Position = [cx, cy]
        self.Size = [100, 50]
        self.Team = team
        image = pygame.transform.scale(pygame.image.load(os.path.join('Assets\\Game\\SoccerGoal.png')), (self.Size[0], self.Size[1]))
        if team == 0:
            self.Image = pygame.transform.rotate(image, 90)
        else:
            self.Image = pygame.transform.rotate(image, -90)

    def Draw(self, pos, state):
        collide = Global.WIN.blit(self.Image, (self.Position[0] + 20, self.Position[1] - 20))
        if state == 0:
            if (collide.collidepoint(pos[0], pos[1])):
                return True
        return False

