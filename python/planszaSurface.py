# type:ignore

import pygame
from pygame.locals import *
from plansza import Plansza
from plansza import Pole
from itertools import product
import time


class planszaSurface:
    # POLE_SZEROKOSC =
    POLE_SZEROKOSC = 50
    OKNO_SZEROKOSC = 640
    OKNO_WYSOKOSC = 480

    FPS = 30  # frames per second to update the screen

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

    BGCOLOR = (40, 40, 40)

    def __init__(self, n_row: int, n_col: int, plansza: Plansza):
        self.n_row = n_row
        self.n_col = n_col

        # inicjuję pygame
        pygame.init()

        # zegar
        FPSCLOCK = pygame.time.Clock()

        # okno
        self.display_surf = pygame.display.set_mode(
            (self.OKNO_SZEROKOSC, self.OKNO_WYSOKOSC)
        )
        pygame.display.set_caption("Four in a Row")

        # odczytuję i przygotowuję krążki
        # czerwony_img = pygame.image.load()

        # odczytuję wygląd pola ramki
        self.pole_img = pygame.image.load("python/media/4row_board.png")
        self.pole_img = pygame.transform.smoothscale(
            self.pole_img, (self.POLE_SZEROKOSC, self.POLE_SZEROKOSC)
        )

        # odczytuję wygląd krążków
        zolty_img = pygame.image.load("python/media/4row_yellow.png")
        zolty_img = pygame.transform.smoothscale(
            zolty_img, (self.POLE_SZEROKOSC, self.POLE_SZEROKOSC)
        )
        czerw_img = pygame.image.load("python/media/4row_red.png")
        czerw_img = pygame.transform.smoothscale(
            czerw_img, (self.POLE_SZEROKOSC, self.POLE_SZEROKOSC)
        )
        self.images = {Pole.zolty: zolty_img, Pole.czerwony: czerw_img}

        self.X_MARGIN = int(
            (self.OKNO_SZEROKOSC - Plansza.n_col * self.POLE_SZEROKOSC) / 2
        )
        self.Y_MARGIN = int(
            (self.OKNO_WYSOKOSC - Plansza.n_row * self.POLE_SZEROKOSC) / 2
        )
        self.plansza = plansza

    def gorny_lewy_rog_pola(self, i, j):
        x = self.X_MARGIN + j * self.POLE_SZEROKOSC
        y = self.OKNO_WYSOKOSC - self.Y_MARGIN - (i + 1) * self.POLE_SZEROKOSC
        return (x, y)

    def srodek_pola(self, i: int, j: int):
        x, y = self.gorny_lewy_rog_pola(i, j)
        x += 0.5 * self.POLE_SZEROKOSC
        y += 0.5 * self.POLE_SZEROKOSC
        return (x, y)

    def rysuj_pole(self, i, j):
        # rysuję krążki. Uwaga! Krążki z wiersza 0 rysowane są na dole
        # for i in range(self.n_row):
        #   for j in range(self.n_col):

        obszar_rect = pygame.Rect(0, 0, self.POLE_SZEROKOSC, self.POLE_SZEROKOSC)
        pole_kolor = self.plansza[i][j]

        if pole_kolor != Pole.puste:
            obszar_rect.center = self.srodek_pola(i, j)
            self.display_surf.blit(self.images[pole_kolor], obszar_rect)

        obszar_rect.topleft = self.gorny_lewy_rog_pola(i, j)
        self.display_surf.blit(self.pole_img, obszar_rect)

    def rysuj_plansze(self):
        # wypełniam tło
        self.display_surf.fill(self.BGCOLOR)

        for i, j in product(range(self.n_row), range(self.n_col)):
            self.rysuj_pole(i, j)

        pygame.display.update()

    def __del__(self):
        pygame.quit()


if __name__ == "__main__":
    plan = Plansza()
    plan.plansza[0][0] = Pole.czerwony
    plan.plansza[0][1] = Pole.zolty
    pS = planszaSurface(plan.n_row, plan.n_col, plan.plansza)
    pS.rysuj_plansze()
    plan.print()
    time.sleep(5)
