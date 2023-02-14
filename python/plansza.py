import builtins
from typing import Optional
import fastenum


class Pole(fastenum.Enum):
    puste = 0
    zolty = 1
    czerwony = 2


# Zwraca kolor przeciwny do podanego
def rev(kolor: Pole) -> Pole:
    if kolor == Pole.zolty:
        return Pole.czerwony
    else:
        return Pole.zolty


#          j
#     _        _
#    |          |
#  i |          |
#    |          |
#     -        -


class Plansza:
    n_col = 7  # liczba kolumn
    n_row = 6  # liczba wierszy

    def __init__(self):
        # będzie to zatem lista wierszy. Pierwszy indeks dla plansza[i][j]
        # przebiega pionowo. Jest to struktura złożona z wierszy
        self.plansza = [
            [Pole.puste for _ in range(self.n_col)] for _ in range(self.n_row)
        ]

        # zbiór współrzędnych pól do specjalnego oznaczenia
        # stosowane między innymi do oznaczenia wygranej
        self.oznaczone = []

        # informacja, o numerze wiersza, w którym leży żeton najwyżej położony
        # w danej kolumnie. Na początku, sokoro nie ma jeszcze żetonów
        # wartość wynosi None
        self.ostatni_w_kolumnie: list[Optional[int]] = [None] * self.n_col

    # Czyści planszę
    def czysc(self):
        for col in range(self.n_col):
            for row in range(self.n_row):
                self.plansza[row][col] = Pole.puste

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
                Pole.czerwony,
            ),
            (
                Pole.czerwony,
                Pole.czerwony,
                Pole.zolty,
                Pole.zolty,
                Pole.czerwony,
                Pole.czerwony,
                Pole.zolty,
            ),
        )

        for row in range(self.n_row):
            ktory = row % 2
            for col in range(self.n_col):
                self.plansza[row][col] = kol_do_wypel[ktory][col]

    def czy_koniec(self):
        fun = self.czy_koniec_fun_gen()
        return fun()

    def czy_koniec_fun_gen(self):
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

        def aby_koniec() -> tuple[bool, Pole]:
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

        return aby_koniec

    def isWinner(self, tile: Pole):
        # check horizontal spaces
        for x in range(self.n_row - 3):
            for y in range(self.n_col):
                if (
                    self.plansza[x][y] == tile
                    and self.plansza[x + 1][y] == tile
                    and self.plansza[x + 2][y] == tile
                    and self.plansza[x + 3][y] == tile
                ):
                    return True
        # check vertical spaces
        for x in range(self.n_row):
            for y in range(self.n_col - 3):
                if (
                    self.plansza[x][y] == tile
                    and self.plansza[x][y + 1] == tile
                    and self.plansza[x][y + 2] == tile
                    and self.plansza[x][y + 3] == tile
                ):
                    return True
        # check / diagonal spaces
        for x in range(self.n_row - 3):
            for y in range(3, self.n_col):
                if (
                    self.plansza[x][y] == tile
                    and self.plansza[x + 1][y - 1] == tile
                    and self.plansza[x + 2][y - 2] == tile
                    and self.plansza[x + 3][y - 3] == tile
                ):
                    return True
        # check \ diagonal spaces
        for x in range(self.n_row - 3):
            for y in range(self.n_col - 3):
                if (
                    self.plansza[x][y] == tile
                    and self.plansza[x + 1][y + 1] == tile
                    and self.plansza[x + 2][y + 2] == tile
                    and self.plansza[x + 3][y + 3] == tile
                ):
                    return True
        return False

    def isWinner(self, tile: Pole) -> bool:
        # check horizontal spaces
        for x in range(self.n_row - 3):
            for y in range(self.n_col):
                if self.plansza[x][y] != tile:
                    continue
                if self.plansza[x + 1][y] != tile:
                    continue
                if self.plansza[x + 2][y] != tile:
                    continue
                if self.plansza[x + 3][y] != tile:
                    continue
                return True
        # check vertical spaces
        for x in range(self.n_row):
            for y in range(self.n_col - 3):
                if self.plansza[x][y] != tile:
                    continue
                if self.plansza[x][y + 1] != tile:
                    continue
                if self.plansza[x][y + 2] != tile:
                    continue
                if self.plansza[x][y + 3] != tile:
                    continue
                return True
        # check / diagonal spaces
        for x in range(self.n_row - 3):
            for y in range(3, self.n_col):
                if (
                    self.plansza[x][y] == tile
                    and self.plansza[x + 1][y - 1] == tile
                    and self.plansza[x + 2][y - 2] == tile
                    and self.plansza[x + 3][y - 3] == tile
                ):
                    return True
        # check \ diagonal spaces
        for x in range(self.n_row - 3):
            for y in range(self.n_col - 3):
                if (
                    self.plansza[x][y] == tile
                    and self.plansza[x + 1][y + 1] == tile
                    and self.plansza[x + 2][y + 2] == tile
                    and self.plansza[x + 3][y + 3] == tile
                ):
                    return True
        return False

    def czy_koniec(self):
        if self.isWinner(Pole.zolty):
            return (True, Pole.zolty)
        if self.isWinner(Pole.czerwony):
            return (True, Pole.czerwony)
        return (False, None)

    # sprawdz, czy wrzucenie żetony do col kolumny zakończyło grę
    def czy_konczacy_ruch(self, col: int) -> bool:
        return True

    def czy_wygrany_ruch_prawo_dol(self, i0: int, j0: int):
        # print("x4")
        # czy / jest wygrana

        kolor = self.plansza[i0][j0]
        i_max = self.n_row - 1
        j_max = self.n_col - 1

        b = i0 + j0

        # miejsce przecięcia z górną krawędzią
        j_prz = b - i_max

        # czy przecięliśmy w zakresie
        if j_prz >= 0:
            j_start = j_prz
            i_start = -j_start + b
        else:
            j_start = 0
            i_start = b

        # ile możliwych kroków do wykonania zanim trafimy na którąś
        # ścianę, z zapsem 3 kroków
        ile_krokow = min(i_start, j_max - j_start) - 3

        for delta in range(ile_krokow + 1):
            i = i_start - delta
            j = j_start + delta
            if (
                self.plansza[i][j] == kolor
                and self.plansza[i - 1][j + 1] == kolor
                and self.plansza[i - 2][j + 2] == kolor
                and self.plansza[i - 3][j + 3] == kolor
            ):
                return True
        return False

    def czy_wygrany_ruch_lewo_dol(self, i0: int, j0: int):
        # print("x4")
        # czy / jest wygrana

        kolor = self.plansza[i0][j0]
        i_max = self.n_row - 1
        j_max = self.n_col - 1

        b = i0 - j0

        # miejsce przecięcia z górną krawędzią
        j_prz = i_max - b

        # czy przecięliśmy w zakresie
        if j_prz <= j_max:
            j_start = j_prz
            i_start = i_max
        else:
            j_start = j_max
            i_start = j_start + b

        # czy jest możliwe 4 po skosie
        ile_krokow = min(j_start, i_start) - 3

        for delta in range(ile_krokow + 1):
            i = i_start - delta
            j = j_start - delta
            if (
                self.plansza[i][j] == kolor
                and self.plansza[i - 1][j - 1] == kolor
                and self.plansza[i - 2][j - 2] == kolor
                and self.plansza[i - 3][j - 3] == kolor
            ):
                return True
        return False

    def czy_wygrany_ruch(self, col: int) -> bool:
        i0 = self.ostatni_w_kolumnie[col]
        j0 = col
        kolor = self.plansza[i0][j0]

        if kolor == Pole.puste:
            return False

        # print("x1")
        # czy w pionie jest wygrana
        if i0 >= 3:
            i = i0
            if (
                self.plansza[i][j0] == kolor
                and self.plansza[i - 1][j0] == kolor
                and self.plansza[i - 2][j0] == kolor
                and self.plansza[i - 3][j0] == kolor
            ):
                return True

        # print("x2")
        # czy w poziomie jest wygrana
        for j in range(self.n_col - 3):
            if (
                self.plansza[i0][j] == kolor
                and self.plansza[i0][j + 1] == kolor
                and self.plansza[i0][j + 2] == kolor
                and self.plansza[i0][j + 3] == kolor
            ):
                return True

        if self.czy_wygrany_ruch_lewo_dol(i0, j0):
            return True

        if self.czy_wygrany_ruch_prawo_dol(i0, j0):
            return True

        return False

    def print(self):
        builtins.print()
        builtins.print()

        for row in reversed(range(self.n_row)):
            builtins.print("|", end="")
            for col in range(self.n_col):
                if self.plansza[row][col] == Pole.puste:
                    builtins.print(" ", end="")
                elif self.plansza[row][col] == Pole.zolty:
                    builtins.print("\033[0;33;40mO\033[0;00;00m", end="")
                elif self.plansza[row][col] == Pole.czerwony:
                    builtins.print("\033[0;31;40mO\033[0;00;00m", end="")
                builtins.print("|", end="")
            builtins.print("")

        for col in range(self.n_col * 2 + 1):
            builtins.print("-", end="")
        builtins.print("")
        for col in range(self.n_col):
            builtins.print("|", end="")
            builtins.print(col, end="")
        builtins.print("|")
        for col in range(self.n_col * 2 + 1):
            builtins.print("=", end="")

        builtins.print("")

    # Wrzuca w j-tą kolumnę klocek o kolorze kolor
    # Jeśli dana kolumna była już pełna, zwraca False
    def wrzuc(self, col: int, kolor: Pole) -> bool:
        row = self.ostatni_w_kolumnie[col]
        if row is None:
            row = 0
        else:
            row += 1

        if row < self.n_row:
            self.plansza[row][col] = kolor
            self.ostatni_w_kolumnie[col] = row
            return True
        else:
            return False

    # W którym wierszu znajduje się najwyższy żeton w kolumnie j
    def gdzie_ostatni(self, col: int) -> Optional[int]:
        return self.ostatni_w_kolumnie[col]

    # Wyjmuje klocek z j-tej kolumny
    def wyjmij(self, col: int):
        row = self.ostatni_w_kolumnie[col]
        if row is None:
            return
        self.plansza[row][col] = Pole.puste
        if row == 0:
            self.ostatni_w_kolumnie[col] = None
        else:
            self.ostatni_w_kolumnie[col] = row - 1

    # def hash_string(self):
    #     wyn = ""
    #     for wiersz in self.plansza:
    #         wyn += "".join(str(e.value) for e in wiersz)
    #     return wyn

    def __repr__(self) -> str:
        wyn = ""
        for wiersz in reversed(self.plansza):
            wyn += "|".join(str(e.value) for e in wiersz) + "\n"
        return wyn

        return tuple(row_to_int(row) for row in self.plansza)

    def hash_string(self) -> tuple[int]:
        def row_to_int(row: list[Pole]) -> int:
            return (
                row[0].value
                | (row[1].value << 2)
                | (row[2].value << 4)
                | (row[3].value << 6)
                | (row[4].value << 8)
                | (row[5].value << 10)
                | (row[6].value << 12)
            )

        return tuple(row_to_int(row) for row in self.plansza)
