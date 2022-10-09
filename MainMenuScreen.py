import pygame
import os
import Global

class MainMenuScreen(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.BackGround = pygame.transform.scale(pygame.image.load(os.path.join('Assets\\Main Menu\\background.jpg')), (Global.WIDTH, Global.HEIGHT))
        self.Button = pygame.transform.scale(pygame.image.load(os.path.join('Assets\\Main Menu\\Button.png')), (400, 75))
        self.Font = pygame.font.SysFont('comicsans', 40)
        self.EventPos = [0, 0]
        self.Run = True

    def Draw(self):
        Global.WIN.blit(self.BackGround, (0, 0))
        Logo = self.Font.render("Mini Football", 1, (0, 255, 0))  # red
        Global.WIN.blit(Logo, (400, 50))
        # Draw Play Button
        btn_copy = self.Button
        collinde = Global.WIN.blit(btn_copy, (300, 150))
        if (collinde.collidepoint(self.EventPos[0], self.EventPos[1])):
            Global.SCREENID += 1
            Global.MODE = 0
            Global.SCREEN_RESET = True
        Text = self.Font.render("Play", 1, (0, 0, 255))  # red
        Global.WIN.blit(Text, (475, 160))
        # Draw 1 vs 1 Button
        btn_copy = self.Button
        collinde = Global.WIN.blit(btn_copy, (300, 300))
        if (collinde.collidepoint(self.EventPos[0], self.EventPos[1])):
            Global.SCREENID += 1
            Global.MODE = 1
            Global.SCREEN_RESET = True
        Text = self.Font.render("1 vs 1", 1, (0, 0, 255))  # red
        Global.WIN.blit(Text, (455, 310))
        # Draw Exit Button
        btn_copy = self.Button
        collinde = Global.WIN.blit(btn_copy, (300, 450))
        if (collinde.collidepoint(self.EventPos[0], self.EventPos[1])):
            self.Run = False
        Text = self.Font.render("Exit", 1, (0, 0, 255))  # red
        Global.WIN.blit(Text, (460, 460))

    def Input(self, run):
        if self.Run == False:
            return False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                self.EventPos[0], self.EventPos[1] = event.pos
        return run

    def Reset(self):
        pass