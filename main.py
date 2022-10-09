import pygame
import Global
import GameScreen
import MainMenuScreen

def main():
    run = True
    clock = pygame.time.Clock()
    Screen = [MainMenuScreen.MainMenuScreen(), GameScreen.GameScreen(Global.MODE)]
    Screen[Global.SCREENID].Reset()
    while run:
        if Global.SCREEN_RESET:
            Screen[Global.SCREENID].Reset()
            Global.SCREEN_RESET = False
        clock.tick(Global.FPS)
        run = Screen[Global.SCREENID].Input(run)
        Screen[Global.SCREENID].Draw()
        pygame.display.update()

if __name__ == "__main__":
    pygame.init()
    main()
    pygame.quit()