import enum
import builtins


class Pole(enum.Enum):
    puste = 0
    zolty = 1
    czerwony = 2


# Zwraca kolor przeciwny do podanego
def rev(kolor: Pole) -> Pole:
    if kolor == Pole.zolty:
        return Pole.czerwony
    else:
        return Pole.zolty


class Plansza:
    n_col = 7
    n_row = 6

    def __init__(self):
        self.plansza = [
            [Pole.puste for _ in range(self.n_col)] for _ in range(self.n_row)
        ]

        # zbiór współrzędnych pól do specjalnego oznaczenia
        # stosowane między innymi do oznaczenia wygranej
        self.oznaczone = []

    # Czyści planszę
    def czysc(self):
        for i in range(self.n_row):
            for j in range(self.n_col):
                self.plansza[i][j] = Pole.puste

    # Wypełnia planszę tak, aby nie było wygranej
    # przydatne do testowania
    def wypelnij(self):
        kol_do_wypel = (
            (
                Pole.zolty,
                Pole.zolty,
                Pole.czerwony,
                Pole.czerwony,
                Pole.zolty,
                Pole.zolty,
            ),
            (
                Pole.czerwony,
                Pole.czerwony,
                Pole.zolty,
                Pole.zolty,
                Pole.czerwony,
                Pole.czerwony,
            ),
        )

        for j in range(self.n_col):
            ktory = j % 2
            for i in range(self.n_row):
                self.plansza[i][j] = kol_do_wypel[ktory][i]

    def czy_koniec(self) -> tuple[bool, Pole]:
        kierunki = ((0, 1), (1, 0), (1, 1), (-1, 1))

        startowe = (
            # dla kierunku poziomego
            ((i, 0) for i in range(self.n_row)),
            # dla kierunku pionowego
            ((0, j) for j in range(self.n_col)),
            # dla skosu w prawo i górę
            ((2, 0), (1, 0), (0, 0), (0, 1), (0, 2), (0, 3)),
            # dla skosu w prawo i w dół
            ((3, 0), (4, 0), (5, 0), (5, 1), (5, 2), (5, 3)),
        )

        for (i_delta, j_delta), startowy in zip(kierunki, startowe):
            for punkt_startu in startowy:
                ile_zoltych = 0
                ile_czerwonych = 0
                i = punkt_startu[0]
                j = punkt_startu[1]

                while i >= 0 and i < self.n_row and j >= 0 and j < self.n_col:
                    if self.plansza[i][j] == Pole.zolty:
                        ile_zoltych = ile_zoltych + 1
                        ile_czerwonych = 0
                        if ile_zoltych == 4:
                            return (True, Pole.zolty)

                    elif self.plansza[i][j] == Pole.czerwony:
                        ile_czerwonych = ile_czerwonych + 1
                        ile_zoltych = 0
                        if ile_czerwonych == 4:
                            return (True, Pole.czerwony)
                    else:
                        ile_zoltych = 0
                        ile_czerwonych = 0
                        # jeśli nie zmieszczą się już 4 w rzędzie,
                        # to wychodzę z pętli
                        if (
                            i + 4 * i_delta < 0
                            or i + 4 * i_delta >= self.n_row
                            or j + 4 * j_delta < 0
                            or j + 4 * j_delta >= self.n_row
                        ):
                            break

                    i = i + i_delta
                    j = j + j_delta

        return (False, None)  # type: ignore

    def print(self):
        builtins.print()
        builtins.print()

        for i in reversed(range(self.n_row)):
            builtins.print("|", end="")
            for j in range(self.n_col):
                if self.plansza[i][j] == Pole.puste:
                    builtins.print(" ", end="")
                elif self.plansza[i][j] == Pole.zolty:
                    builtins.print("\033[0;33;40mO\033[0;00;00m", end="")
                elif self.plansza[i][j] == Pole.czerwony:
                    builtins.print("\033[0;31;40mO\033[0;00;00m", end="")
                builtins.print("|", end="")
            builtins.print("")

        for j in range(self.n_col * 2 + 1):
            builtins.print("-", end="")
        builtins.print("")
        for j in range(self.n_col):
            builtins.print("|", end="")
            builtins.print(j, end="")
        builtins.print("|")
        for j in range(self.n_col * 2 + 1):
            builtins.print("=", end="")

        builtins.print("")

    # Wrzuca w j-tą kolumnę klocek o kolorze kolor
    # Jeśli dana kolumna była już pełna, zwraca False
    def wrzuc(self, j: int, kolor: Pole) -> bool:
        i = 0
        while i < self.n_row and self.plansza[i][j] != Pole.puste:
            i = i + 1

        if i < self.n_row:
            self.plansza[i][j] = kolor
            return True
        else:
            return False

    # Wyjmuje klocek z j-tej kolumny
    def wyjmij(self, j: int):
        i = self.n_row - 1
        while i >= 0 and self.plansza[i][j] == Pole.puste:
            i = i - 1
        self.plansza[i][j] = Pole.puste

    def hash_string(self):
        wyn = ""
        for wiersz in self.plansza:
            wyn += "".join(str(e.value) for e in wiersz)
        return wyn

    def __repr__(self) -> str:
        wyn = ""
        for wiersz in reversed(self.plansza):
            wyn += "|".join(str(e.value) for e in wiersz) + "\n"
        return wyn
