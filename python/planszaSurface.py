import pygame
from pygame.locals import *
from plansza import Plansza as p
import time


class planszaSurface:

    #POLE_SZEROKOSC = 
    POLE_SZEROKOSC = 50
    OKNO_SZEROKOSC = 640
    OKNO_WYSOKOSC = 480

    FPS = 30 # frames per second to update the screen

    X_MARGIN = None
    Y_MARGIN = None
    plansza = None

    display_surf = None

    # grafiki
    pole_img = None
    czerw_img = None
    zolty_img = None

    # liczba kolumn i wierszy w planszy. Na przyszłość przerzucić
    # to do klasy planszy bo inaczej nie ma to sensu
    n_row = None
    n_col = None

    # definicje kolorów
    BRIGHTBLUE = (0, 50, 255)
    WHITE = (255, 255, 255)

    BGCOLOR = BRIGHTBLUE

    def __init__(self, n_row, n_col, plansza):

        self.n_row = n_row
        self.n_col = n_col

        # inicjuję pygame
        pygame.init()

        # zegar
        FPSCLOCK = pygame.time.Clock()

        # okno
        self.display_surf = pygame.display.set_mode((self.OKNO_SZEROKOSC, self.OKNO_WYSOKOSC))
        pygame.display.set_caption('Four in a Row')

        # odczytuję i przygotowuję krążki
        #czerwony_img = pygame.image.load()

        # odczytuję wygląd pola ramki
        self.pole_img = pygame.image.load('media/4row_board.png')
        self.pole_img = pygame.transform.smoothscale(self.pole_img, (self.POLE_SZEROKOSC, self.POLE_SZEROKOSC))

        # odczytuję wygląd krążków
        self.zol_img = pygame.image.load('media/4row_yellow.png')
        self.zol_img = pygame.transform.smoothscale(self.zol_img, (self.POLE_SZEROKOSC, self.POLE_SZEROKOSC))
        self.czerw_img = pygame.image.load('media/4row_red.png')
        self.czerw_img = pygame.transform.smoothscale(self.czerw_img, (self.POLE_SZEROKOSC, self.POLE_SZEROKOSC))

        self.X_MARGIN = int((self.OKNO_SZEROKOSC - p.n_col * self.POLE_SZEROKOSC) / 2)
        self.Y_MARGIN = int((self.OKNO_WYSOKOSC - p.n_row * self.POLE_SZEROKOSC) / 2)
        self.plansza = plansza


    def rysuj(self):

        obszar_rect = pygame.Rect(0, 0, self.POLE_SZEROKOSC, self.POLE_SZEROKOSC) 

        # wypełniam tło
        self.display_surf.fill(self.BRIGHTBLUE)

        # rysuję krążki. Uwaga! Krążki z wiersza 0 rysowane są na dole
        for i in range(self.n_row):
            for j in range(self.n_col):
                x = self.X_MARGIN + j*self.POLE_SZEROKOSC + 0.5*self.POLE_SZEROKOSC
                y = self.OKNO_WYSOKOSC - self.Y_MARGIN - i*self.POLE_SZEROKOSC - 0.5*self.POLE_SZEROKOSC
                obszar_rect.center = (x,y)
                if self.plansza[i][j] == p.Pole.zolty:
                    self.display_surf.blit(self.zol_img, obszar_rect)
                if self.plansza[i][j] == p.Pole.czerwony:
                    self.display_surf.blit(self.czerw_img, obszar_rect)

        # rysuję ramkę
        for i in range(self.n_row):
            for j in range(self.n_col):
                x = self.X_MARGIN + j*self.POLE_SZEROKOSC 
                y = self.Y_MARGIN + i*self.POLE_SZEROKOSC
                obszar_rect.topleft = (x,y)
                self.display_surf.blit(self.pole_img, obszar_rect)

        pygame.display.update()

    def __del__(self):
        pygame.quit()


if __name__ == '__main__':
    p.plansza[0][0] = p.Pole.czerwony
    p.plansza[0][1] = p.Pole.zolty
    pS = planszaSurface(p.n_row, p.n_col, p.plansza)
    pS.rysuj()
    time.sleep(5)  
    


