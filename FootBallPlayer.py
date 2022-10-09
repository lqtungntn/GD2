import pygame
import os
import Global

class FootBallPlayer(pygame.sprite.Sprite):
    def __init__(self, cx, cy, team):
        super().__init__()
        self.ListImage = [[], [], []]
        self.Size = [50, 50]
        self.Team = team
        if team == 0:
            # Picture Run
            self.ListImage[0].append(pygame.transform.scale(pygame.image.load(os.path.join('Assets\\Game\\Player\\Player1_Run_0.png')), (self.Size[0], self.Size[1])))
            self.ListImage[0].append(pygame.transform.scale(pygame.image.load(os.path.join('Assets\\Game\\Player\\Player1_Run_1.png')), (self.Size[0], self.Size[1])))
            self.ListImage[0].append(pygame.transform.scale(pygame.image.load(os.path.join('Assets\\Game\\Player\\Player1_Run_2.png')), (self.Size[0], self.Size[1])))
            self.ListImage[0].append(pygame.transform.scale(pygame.image.load(os.path.join('Assets\\Game\\Player\\Player1_Run_3.png')), (self.Size[0], self.Size[1])))
            self.ListImage[0].append(pygame.transform.scale(pygame.image.load(os.path.join('Assets\\Game\\Player\\Player1_Run_4.png')), (self.Size[0], self.Size[1])))
            self.ListImage[0].append(pygame.transform.scale(pygame.image.load(os.path.join('Assets\\Game\\Player\\Player1_Run_5.png')), (self.Size[0], self.Size[1])))
            self.ListImage[0].append(pygame.transform.scale(pygame.image.load(os.path.join('Assets\\Game\\Player\\Player1_Run_6.png')), (self.Size[0], self.Size[1])))
            self.ListImage[0].append(pygame.transform.scale(pygame.image.load(os.path.join('Assets\\Game\\Player\\Player1_Run_7.png')), (self.Size[0], self.Size[1])))
            self.ListImage[0].append(pygame.transform.scale(pygame.image.load(os.path.join('Assets\\Game\\Player\\Player1_Run_8.png')), (self.Size[0], self.Size[1])))
            self.ListImage[0].append(pygame.transform.scale(pygame.image.load(os.path.join('Assets\\Game\\Player\\Player1_Run_9.png')), (self.Size[0], self.Size[1])))
            # Picture Tackle
            self.ListImage[1].append(pygame.transform.scale(pygame.image.load(os.path.join('Assets\\Game\\Player\\Player1_Slide_0.png')), (self.Size[0], self.Size[1])))
            self.ListImage[1].append(pygame.transform.scale(pygame.image.load(os.path.join('Assets\\Game\\Player\\Player1_Slide_1.png')), (self.Size[0], self.Size[1])))
            self.ListImage[1].append(pygame.transform.scale(pygame.image.load(os.path.join('Assets\\Game\\Player\\Player1_Slide_2.png')), (self.Size[0], self.Size[1])))
            self.ListImage[1].append(pygame.transform.scale(pygame.image.load(os.path.join('Assets\\Game\\Player\\Player1_Slide_3.png')), (self.Size[0], self.Size[1])))
            self.ListImage[1].append(pygame.transform.scale(pygame.image.load(os.path.join('Assets\\Game\\Player\\Player1_Slide_4.png')), (self.Size[0], self.Size[1])))
            self.ListImage[1].append(pygame.transform.scale(pygame.image.load(os.path.join('Assets\\Game\\Player\\Player1_Slide_5.png')), (self.Size[0], self.Size[1])))
            self.ListImage[1].append(pygame.transform.scale(pygame.image.load(os.path.join('Assets\\Game\\Player\\Player1_Slide_6.png')), (self.Size[0], self.Size[1])))
            self.ListImage[1].append(pygame.transform.scale(pygame.image.load(os.path.join('Assets\\Game\\Player\\Player1_Slide_7.png')), (self.Size[0], self.Size[1])))
            # Picture Shoot
            self.ListImage[2].append(pygame.transform.scale(pygame.image.load(os.path.join('Assets\\Game\\Player\\Player1_Shoot_0.png')), (self.Size[0], self.Size[1])))
            self.ListImage[2].append(pygame.transform.scale(pygame.image.load(os.path.join('Assets\\Game\\Player\\Player1_Shoot_1.png')), (self.Size[0], self.Size[1])))
            self.ListImage[2].append(pygame.transform.scale(pygame.image.load(os.path.join('Assets\\Game\\Player\\Player1_Shoot_2.png')), (self.Size[0], self.Size[1])))
            self.ListImage[2].append(pygame.transform.scale(pygame.image.load(os.path.join('Assets\\Game\\Player\\Player1_Shoot_3.png')), (self.Size[0], self.Size[1])))
            self.ListImage[2].append(pygame.transform.scale(pygame.image.load(os.path.join('Assets\\Game\\Player\\Player1_Shoot_4.png')), (self.Size[0], self.Size[1])))
            self.ListImage[2].append(pygame.transform.scale(pygame.image.load(os.path.join('Assets\\Game\\Player\\Player1_Shoot_5.png')), (self.Size[0], self.Size[1])))
            self.ListImage[2].append(pygame.transform.scale(pygame.image.load(os.path.join('Assets\\Game\\Player\\Player1_Shoot_6.png')), (self.Size[0], self.Size[1])))
            self.ListImage[2].append(pygame.transform.scale(pygame.image.load(os.path.join('Assets\\Game\\Player\\Player1_Shoot_7.png')), (self.Size[0], self.Size[1])))
            self.ListImage[2].append(pygame.transform.scale(pygame.image.load(os.path.join('Assets\\Game\\Player\\Player1_Shoot_8.png')), (self.Size[0], self.Size[1])))
        else:
            # Picture Run
            self.ListImage[0].append(pygame.transform.scale(pygame.image.load(os.path.join('Assets\\Game\\Player\\Player2_Run_0.png')), (self.Size[0], self.Size[1])))
            self.ListImage[0].append(pygame.transform.scale(pygame.image.load(os.path.join('Assets\\Game\\Player\\Player2_Run_1.png')), (self.Size[0], self.Size[1])))
            self.ListImage[0].append(pygame.transform.scale(pygame.image.load(os.path.join('Assets\\Game\\Player\\Player2_Run_2.png')), (self.Size[0], self.Size[1])))
            self.ListImage[0].append(pygame.transform.scale(pygame.image.load(os.path.join('Assets\\Game\\Player\\Player2_Run_3.png')), (self.Size[0], self.Size[1])))
            self.ListImage[0].append(pygame.transform.scale(pygame.image.load(os.path.join('Assets\\Game\\Player\\Player2_Run_4.png')), (self.Size[0], self.Size[1])))
            self.ListImage[0].append(pygame.transform.scale(pygame.image.load(os.path.join('Assets\\Game\\Player\\Player2_Run_5.png')), (self.Size[0], self.Size[1])))
            self.ListImage[0].append(pygame.transform.scale(pygame.image.load(os.path.join('Assets\\Game\\Player\\Player2_Run_6.png')), (self.Size[0], self.Size[1])))
            self.ListImage[0].append(pygame.transform.scale(pygame.image.load(os.path.join('Assets\\Game\\Player\\Player2_Run_7.png')), (self.Size[0], self.Size[1])))
            self.ListImage[0].append(pygame.transform.scale(pygame.image.load(os.path.join('Assets\\Game\\Player\\Player2_Run_8.png')), (self.Size[0], self.Size[1])))
            self.ListImage[0].append(pygame.transform.scale(pygame.image.load(os.path.join('Assets\\Game\\Player\\Player2_Run_9.png')), (self.Size[0], self.Size[1])))
            # Picture Tackle
            self.ListImage[1].append(pygame.transform.scale(pygame.image.load(os.path.join('Assets\\Game\\Player\\Player2_Slide_0.png')), (self.Size[0], self.Size[1])))
            self.ListImage[1].append(pygame.transform.scale(pygame.image.load(os.path.join('Assets\\Game\\Player\\Player2_Slide_1.png')), (self.Size[0], self.Size[1])))
            self.ListImage[1].append(pygame.transform.scale(pygame.image.load(os.path.join('Assets\\Game\\Player\\Player2_Slide_2.png')), (self.Size[0], self.Size[1])))
            self.ListImage[1].append(pygame.transform.scale(pygame.image.load(os.path.join('Assets\\Game\\Player\\Player2_Slide_3.png')), (self.Size[0], self.Size[1])))
            self.ListImage[1].append(pygame.transform.scale(pygame.image.load(os.path.join('Assets\\Game\\Player\\Player2_Slide_4.png')), (self.Size[0], self.Size[1])))
            self.ListImage[1].append(pygame.transform.scale(pygame.image.load(os.path.join('Assets\\Game\\Player\\Player2_Slide_5.png')), (self.Size[0], self.Size[1])))
            self.ListImage[1].append(pygame.transform.scale(pygame.image.load(os.path.join('Assets\\Game\\Player\\Player2_Slide_6.png')), (self.Size[0], self.Size[1])))
            self.ListImage[1].append(pygame.transform.scale(pygame.image.load(os.path.join('Assets\\Game\\Player\\Player2_Slide_7.png')), (self.Size[0], self.Size[1])))
            # Picture Shoot
            self.ListImage[2].append(pygame.transform.scale(pygame.image.load(os.path.join('Assets\\Game\\Player\\Player2_Shoot_0.png')), (self.Size[0], self.Size[1])))
            self.ListImage[2].append(pygame.transform.scale(pygame.image.load(os.path.join('Assets\\Game\\Player\\Player2_Shoot_1.png')), (self.Size[0], self.Size[1])))
            self.ListImage[2].append(pygame.transform.scale(pygame.image.load(os.path.join('Assets\\Game\\Player\\Player2_Shoot_2.png')), (self.Size[0], self.Size[1])))
            self.ListImage[2].append(pygame.transform.scale(pygame.image.load(os.path.join('Assets\\Game\\Player\\Player2_Shoot_3.png')), (self.Size[0], self.Size[1])))
            self.ListImage[2].append(pygame.transform.scale(pygame.image.load(os.path.join('Assets\\Game\\Player\\Player2_Shoot_4.png')), (self.Size[0], self.Size[1])))
            self.ListImage[2].append(pygame.transform.scale(pygame.image.load(os.path.join('Assets\\Game\\Player\\Player2_Shoot_5.png')), (self.Size[0], self.Size[1])))
            self.ListImage[2].append(pygame.transform.scale(pygame.image.load(os.path.join('Assets\\Game\\Player\\Player2_Shoot_6.png')), (self.Size[0], self.Size[1])))
            self.ListImage[2].append(pygame.transform.scale(pygame.image.load(os.path.join('Assets\\Game\\Player\\Player2_Shoot_7.png')), (self.Size[0], self.Size[1])))
            self.ListImage[2].append(pygame.transform.scale(pygame.image.load(os.path.join('Assets\\Game\\Player\\Player2_Shoot_8.png')), (self.Size[0], self.Size[1])))
        self.CurImage = 0.0
        self.Position = []
        self.DefaultPos = [cx, cy]
        self.Speed = [0, 0]
        self.FaceDic = 1
        self.VectorDir = [0, 0]
        self.State = 0 # 0: run, 1: tackle, 2: shoot/pass
        self.IsAnim = False
        self.HaveBall = False
        self.Hcn = Global.WIN.blit(self.ListImage[0][0], (0, 0))
        self.IsStun = False
        self.Counter = 0
        self.Sound = pygame.mixer.Sound("Sound\\Run.mp3")

    def Draw(self):
        if self.IsStun:
            if self.Counter == Global.FPS:
                self.IsStun = False
            else:
                self.Counter += 1
            self.State = 0
            self.HaveBall = False
            self.Counter += 1
            self.CurImage = 0.0
            self.Speed = [0, 0]
            if (self.FaceDic == 1):
                Image_copy = self.ListImage[self.State][int(self.CurImage)]
            elif (self.FaceDic == -1):
                Image_copy = pygame.transform.flip(self.ListImage[self.State][int(self.CurImage)], True, False)
            self.Hcn = Global.WIN.blit(Image_copy, (self.Position[0], self.Position[1]))
        else:
            if self.State == 0: # run
                self.UpdateImage(max(abs(float(self.Speed[0])), abs(float(self.Speed[1]))) / 5, 10)
                if (self.Speed[0] > 0) or ((self.Speed[0] == 0) and (self.FaceDic == 1)):
                    Image_copy = self.ListImage[self.State][int(self.CurImage)]
                    self.FaceDic = 1
                elif (self.Speed[0] < 0) or ((self.Speed[0] == 0) and (self.FaceDic == -1)):
                    Image_copy = pygame.transform.flip(self.ListImage[self.State][int(self.CurImage)], True, False)
                    self.FaceDic = -1
                self.Position[0] = max(min(self.Position[0] + self.Speed[0], Global.WIDTH - self.Size[0]), 0)
                self.Position[1] = max(min(self.Position[1] + self.Speed[1], Global.HEIGHT - self.Size[0]), 0)
                self.Hcn = Global.WIN.blit(Image_copy, (self.Position[0], self.Position[1]))
            elif self.State == 1: # tackle
                self.UpdateImage(0.2, 8)
                if (self.Speed[0] > 0) or ((self.Speed[0] == 0) and (self.FaceDic == 1)):
                    Image_copy = self.ListImage[self.State][int(self.CurImage)]
                    self.FaceDic = 1
                elif (self.Speed[0] < 0) or ((self.Speed[0] == 0) and (self.FaceDic == -1)):
                    Image_copy = pygame.transform.flip(self.ListImage[self.State][int(self.CurImage)], True, False)
                    self.FaceDic = -1
                self.Position[0] += self.Speed[0]
                self.Position[1] += self.Speed[1]
                self.Hcn = Global.WIN.blit(Image_copy, (self.Position[0], self.Position[1]))
            elif self.State == 2: # shoot
                self.UpdateImage(0.2, 9)
                if (self.Speed[0] > 0) or ((self.Speed[0] == 0) and (self.FaceDic == 1)):
                    Image_copy = self.ListImage[self.State][int(self.CurImage)]
                    self.FaceDic = 1
                elif (self.Speed[0] < 0) or ((self.Speed[0] == 0) and (self.FaceDic == -1)):
                    Image_copy = pygame.transform.flip(self.ListImage[self.State][int(self.CurImage)], True, False)
                    self.FaceDic = -1
                self.Position[0] += self.Speed[0]
                self.Position[1] += self.Speed[1]
                self.Hcn = Global.WIN.blit(Image_copy, (self.Position[0], self.Position[1]))

    def UpdateImage(self, inc, limit):
        self.CurImage = (self.CurImage + inc) % limit
        if self.CurImage - 0.0 < inc:
            self.IsAnim = False
            self.State = 0

    def Input(self, event):
        if self.IsAnim == False:
            if self.Team == 0:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        self.Sound.play(-1)
                        self.Speed[1] = -5
                        self.VectorDir[1] = -1
                        self.State = 0
                    elif event.key == pygame.K_s:
                        self.Sound.play(-1)
                        self.Speed[1] = 5
                        self.VectorDir[1] = 1
                        self.State = 0
                    elif event.key == pygame.K_a:
                        self.Sound.play(-1)
                        self.Speed[0] = -5
                        self.VectorDir[0] = -1
                        self.State = 0
                    elif event.key == pygame.K_d:
                        self.Sound.play(-1)
                        self.Speed[0] = 5
                        self.VectorDir[0] = 1
                        self.State = 0
                    elif event.key == pygame.K_z and self.HaveBall == False:
                        self.State = 1
                        self.IsAnim = True
                        self.CurImage = 0.0
                    elif event.key == pygame.K_x:
                        self.State = 2
                        self.IsAnim = True
                        self.CurImage = 0.0
                        self.HaveBall = False
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_w:
                        self.Sound.stop()
                        self.Speed[1] = 0
                        self.VectorDir[1] = 0
                    elif event.key == pygame.K_s:
                        self.Sound.stop()
                        self.Speed[1] = 0
                        self.VectorDir[1] = 0
                    elif event.key == pygame.K_a:
                        self.Sound.stop()
                        self.Speed[0] = 0
                        self.VectorDir[0] = 0
                    elif event.key == pygame.K_d:
                        self.Sound.stop()
                        self.Speed[0] = 0
                        self.VectorDir[0] = 0
            else:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.Sound.play(-1)
                        self.Speed[1] = -5
                        self.VectorDir[1] = -1
                        self.State = 0
                    elif event.key == pygame.K_DOWN:
                        self.Sound.play(-1)
                        self.Speed[1] = 5
                        self.VectorDir[1] = 1
                        self.State = 0
                    elif event.key == pygame.K_LEFT:
                        self.Sound.play(-1)
                        self.Speed[0] = -5
                        self.VectorDir[0] = -1
                        self.State = 0
                    elif event.key == pygame.K_RIGHT:
                        self.Sound.play(-1)
                        self.Speed[0] = 5
                        self.VectorDir[0] = 1
                        self.State = 0
                    elif event.key == pygame.K_j and self.HaveBall == False:
                        self.State = 1
                        self.IsAnim = True
                        self.CurImage = 0.0
                    elif event.key == pygame.K_k:
                        self.State = 2
                        self.IsAnim = True
                        self.CurImage = 0.0
                        self.HaveBall = False
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        self.Sound.stop()
                        self.Speed[1] = 0
                        self.VectorDir[1] = 0
                    elif event.key == pygame.K_DOWN:
                        self.Sound.stop()
                        self.Speed[1] = 0
                        self.VectorDir[1] = 0
                    elif event.key == pygame.K_LEFT:
                        self.Sound.stop()
                        self.Speed[0] = 0
                        self.VectorDir[0] = 0
                    elif event.key == pygame.K_RIGHT:
                        self.Sound.stop()
                        self.Speed[0] = 0
                        self.VectorDir[0] = 0

    def Reset(self):
        self.Position = self.DefaultPos.copy()
        self.CurImage = 0.0
        self.HaveBall = 0.0
        self.IsAnim = False
        self.IsStun = False
        self.State = 0

    def CheckBall(self, cx, cy):
        return self.Hcn.collidepoint(cx, cy)