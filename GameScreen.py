import pygame
import os

import ArrowPlayer
import Global
import Ball
import FootBallPlayer
import ArrowDirection
import Goal
import Power


class GameScreen(pygame.sprite.Group):
    def __init__(self, mode):
        super().__init__()
        self.BackGround = pygame.transform.scale(pygame.image.load(os.path.join('Assets\\Game\\SoccerField.png')), (Global.WIDTH, Global.HEIGHT))
        self.Result = [0, 0]
        self.Font = pygame.font.SysFont('comicsans', 40)
        self.BallImage = Ball.Ball()
        self.PosFB = [[100, 100], [100, 500], [50, 300], [400, 100], [400, 500], [925, 300], [800, 100], [800, 500], [600, 100], [600, 500]]
        self.FIT = [0,0,0,0,0,1,1,1,1,1] # FootBaller in Team
        self.ListFB = []
        self.SoccerGoal = [Goal.Goal(0, -50, 275), Goal.Goal(1, 910, 275)]
        for idx1, idx2 in zip(self.PosFB, self.FIT):
            self.ListFB.append(FootBallPlayer.FootBallPlayer(idx1[0], idx1[1], idx2))
        self.CurFB = []
        self.CurArrow = []
        for i in range(mode + 1):
            self.CurFB.append(i * 5)
            self.CurArrow.append(ArrowPlayer.ArrowPlayer(i))
        self.AD = ArrowDirection.ArrowDirection()
        self.Pow = Power.Power()
        self.GameState = 0 # 0: running, 1: pause, 2: reset
        self.BGSound = pygame.mixer.Sound("Sound\\Stadium.mp3")
        self.TSound = pygame.mixer.Sound("Sound\\Tackle.wav")
        self.KSound = pygame.mixer.Sound("Sound\\Kick.wav")
        self.GSound = pygame.mixer.Sound("Sound\\Goal.mp3")
        self.WSound = pygame.mixer.Sound("Sound\\Whistle.mp3")
        self.FirstTime = True

    def Draw(self):
        if (self.FirstTime):
            self.WSound.play()
            self.BGSound.play(-1)
            self.FirstTime = False

        #Draw Map
        Global.WIN.blit(self.BackGround, (0, 0))
        for idx in self.SoccerGoal:
            if idx.Draw(self.BallImage.Position, self.GameState):
                self.GSound.play()
                self.Result[1 - idx.Team] += 1
                self.GameState = 2

        #Draw Ball
        if self.BallImage.State == 0:
            temp = self.ListFB[self.BallImage.Player].Position.copy()
            self.BallImage.Position = temp
            self.BallImage.PlayerFaceDir = self.ListFB[self.BallImage.Player].FaceDic
        self.BallImage.Draw()

        #Draw FootBall player
        if self.BallImage.State == 1:
            if self.BallImage.Speed < self.BallImage.Acceleration:
                self.BallImage.Player = -1
                for idx in range(len(self.ListFB)):
                    if self.ListFB[idx].CheckBall(self.BallImage.Position[0], self.BallImage.Position[1]):
                        self.BallImage.Team = self.FIT[idx]
                        self.BallImage.PlayerFaceDir = self.ListFB[idx].FaceDic
                        self.BallImage.State = 0
                        self.BallImage.Player = idx
                        self.ListFB[idx].HaveBall = True
                        break
                    else:
                        self.ListFB[idx].HaveBall = False
            else:
                for idx in range(len(self.ListFB)):
                    if self.ListFB[idx].CheckBall(self.BallImage.Position[0], self.BallImage.Position[1]) and self.BallImage.Player != idx:
                        img = self.ListFB[idx]
                        self.BallImage.CollidePlayer(img)
                        self.BallImage.Player = -1

        for idx in range(len(self.ListFB)):
            self.ListFB[idx].Draw()

        #Draw Arrow Player
        for idx in range(len(self.CurArrow)):
            self.CurArrow[idx].Position = self.ListFB[self.CurFB[idx]].Position.copy()
            self.CurArrow[idx].Draw()

        #Draw Arrow Direction
        if self.GameState == 1:
            self.AD.Position = self.ListFB[self.CurFB[self.BallImage.Team]].Position.copy()
            self.AD.Draw()
            self.Pow.Draw()

        Text = self.Font.render("YOU " + str(self.Result[0]) + " - " + str(self.Result[1]) + " ENEMY", 1, (255, 0, 0))  # yellow
        Global.WIN.blit(Text, (350, 25))

        if self.GameState == 2:
            self.Reset()

    def Input(self, run):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    Global.SCREENID = 0
                    self.FirstTime = True
                    self.BGSound.stop()
                if event.key == pygame.K_z and self.BallImage.Team == 1:
                    self.TSound.play()
                    if self.ListFB[self.CurFB[self.BallImage.Team]].CheckBall(self.BallImage.Position[0], self.BallImage.Position[1]):
                        self.ListFB[self.BallImage.Player].IsStun = True
                        self.BallImage.Team = self.FIT[self.BallImage.Player]
                        self.BallImage.Player = self.CurFB[0]
                elif event.key == pygame.K_x and self.BallImage.Player != -1:
                    self.GameState = 1 - self.GameState
                    if self.GameState == 0:
                        if self.BallImage.Team == 1:
                            self.KSound.play()
                            self.BallImage.GoDir(self.Pow.Energy, self.AD.GetVector())
                        else:
                            self.KSound.play()
                            self.BallImage.GoDir(self.Pow.Energy, self.AD.GetVector())
                    else:
                        self.Pow.Begin = True
                    self.Pow.Energy = 0.0
                elif event.key == pygame.K_f and self.BallImage.State == 1:
                    self.CurFB[0] = (self.CurFB[0] + 1) % 5
                if Global.MODE == 1:
                    if event.key == pygame.K_j and self.BallImage.Team == 0:
                        self.TSound.play()
                        if self.ListFB[self.CurFB[self.BallImage.Team]].CheckBall(self.BallImage.Position[0], self.BallImage.Position[1]):
                            self.ListFB[self.BallImage.Player].IsStun = True
                            self.BallImage.Team = self.FIT[self.BallImage.Player]
                            self.BallImage.Player = self.CurFB[1]
                    elif event.key == pygame.K_k and self.BallImage.Player != -1:
                        self.GameState = 1 - self.GameState
                        if self.GameState == 0:
                            if self.BallImage.Team == 1:
                                self.KSound.play()
                                self.BallImage.GoDir(self.Pow.Energy, self.AD.GetVector())
                            else:
                                self.KSound.play()
                                self.BallImage.GoDir(self.Pow.Energy, self.AD.GetVector())
                        else:
                            self.Pow.Begin = True
                        self.Pow.Energy = 0.0
                    elif event.key == pygame.K_i and self.BallImage.State == 1:
                        self.CurFB[1] = (self.CurFB[1] + 1) % 5 + 5
            if self.GameState == 0:
                for idx in self.CurFB:
                    self.ListFB[idx].Input(event)
            else:
                self.AD.Input(event)
                self.Pow.Input(event, self.BallImage.Team)
        return run

    def Reset(self):
        self.GameState = 0
        self.BallImage.Reset()
        for idx in self.ListFB:
            idx.Reset()