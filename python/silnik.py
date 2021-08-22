from plansza import Plansza
from plansza import Pole
from plansza import rev

class Silnik:

    # wagi do poszczególnych kolumn do oceny pozycji
    wagi_ocena = (0, 0.11, 0.44, 1, 0.44, 0.11, 0)
    zolty_mnoznik = 0.01

    def __init__(self, glebokosc_anal):
        # licznik, ile pozycji końcowych zostało ocenionych
        self.licznik = 0

        # informacyjnie i do wykorzystania w debugowaniu
        self.nr_ruchu = 0
        self.glebokosc_anal = glebokosc_anal

        # Potrzebna do trzymania planszy pomiędzy wywołaniami
        # funkcjami
        self.pl = Plansza()


    def ocen_rozstaw(self, pl: Plansza, kolor: Pole) -> float:
        punkty = 0
        for i in range(pl.n_row):
            for j in range(pl.n_col):
                if pl.plansza[i][j] == kolor:
                    punkty += self.wagi_ocena[j]
        return punkty

    #Ocena z punktu widzenia żółtego
    def ocen(self, pl: Plansza) -> float:

        # czy ktoś wygrał?
        wynik, ktory = pl.czy_koniec()
        if wynik:
            if ktory==Pole.zolty:
                return 100
            else:
                return -100

        # ocena ustawienia krążków
        ocena_z = (1+self.zolty_mnoznik) * self.ocen_rozstaw(pl, Pole.zolty)
        ocena_c = self.ocen_rozstaw(pl, Pole.czerwony)

        return ocena_z - ocena_c



    # szuka najlepszego ruchu. Zwraca go oraz wartość oceny 
    # algorytm minimax
    def minimax(self, akt_gleb, max_gleb, kolor, czy_maks_gracz: bool):
        
        #p.print()

        if akt_gleb > max_gleb:
            self.licznik = self.licznik + 1
            #plansza_print()
            return self.ocen(self.pl)
        
        if czy_maks_gracz:
            best_ocena = -float('inf')
            for j in range(self.pl.n_col):

                #wykonuję ruch
                if self.pl.wrzuc(j, kolor):

                    # sprawdzam, czy koniec
                    # sprawdzam, czy koniec
                    wygrana = self.pl.czy_koniec()[0]

                    # jeśli tak, to wychodzę bo znaleźliśmy najlepszy ruch
                    if wygrana:
                        self.pl.wyjmij(j)
                        return 100

                    #jeśli nie, to zagłębiam się
                    else:
                        wyn = self.minimax(akt_gleb+1, max_gleb, rev(kolor), False)
                        self.pl.wyjmij(j)

                    if wyn > best_ocena:
                        best_ocena = wyn
                
                # Jeśli nie da się wrzucić w dany wiersz
                else:
                    pass


        if not czy_maks_gracz:
            best_ocena = float('inf')
            for j in range(self.pl.n_col):
                if self.pl.wrzuc(j, kolor):

                    # sprawdzam, czy koniec
                    wygrana = self.pl.czy_koniec()[0]

                    # jeśli tak, to wychodzę bo znaleźliśmy najlepszy ruch
                    if wygrana:
                        self.pl.wyjmij(j)
                        return -100                    
                    #jeśli nie, to zagłębiam się
                    else:
                        wyn = self.minimax(akt_gleb+1, max_gleb, rev(kolor), True)
                        self.pl.wyjmij(j)

                    if wyn < best_ocena:
                        best_ocena = wyn
                
                # Jeśli nie da się wrzucić w dany wiersz
                else:
                    pass

        return best_ocena

    # szuka najlepszego ruchu. Zwraca go oraz wartość oceny 
    # algorytm minimax z obcinaniem
    def minimax_obc(self, akt_gleb, max_gleb, kolor, czy_maks_gracz: bool, best_ocena_poprz):
        
        #p.print()

        if akt_gleb > max_gleb:
            global licznik
            licznik = licznik + 1
            #plansza_print()
            return self.ocen(Plansza)
        
        if czy_maks_gracz:
            best_ocena = -float('inf')
            for j in range(self.pl.n_col):

                #wykonuję ruch
                if self.pl.wrzuc(j, kolor):

                    # sprawdzam, czy koniec
                    # sprawdzam, czy koniec
                    wygrana = self.pl.czy_koniec()[0]

                    # jeśli tak, to wychodzę bo znaleźliśmy najlepszy ruch
                    if wygrana:
                        self.pl.wyjmij(j)
                        return 100

                    #jeśli nie, to zagłębiam się
                    else:
                        wyn = self.minimax_obc(akt_gleb+1, max_gleb, rev(kolor), False, best_ocena)
                        self.pl.wyjmij(j)

                    # jeśli nasza odpowiedź już jest lepsza niż nasze odpowiedzi
                    # przy poprzednich ruchach  przeciwnika, to nie ma co dalej
                    # analizować, bo przeciwnik i tak tego ruchu nie wybierze
                    if wyn > best_ocena_poprz:
                        return wyn

                    if wyn > best_ocena:
                        best_ocena = wyn
                
                # Jeśli nie da się wrzucić w dany wiersz
                else:
                    pass


        if not czy_maks_gracz:
            best_ocena = float('inf')
            for j in range(self.pl.n_col):
                if self.pl.wrzuc(j, kolor):

                    # sprawdzam, czy koniec
                    wygrana = self.pl.czy_koniec()[0]

                    # jeśli tak, to wychodzę bo znaleźliśmy najlepszy ruch
                    if wygrana:
                        self.pl.wyjmij(j)
                        return -100                    
                    #jeśli nie, to zagłębiam się
                    else:
                        wyn = self.minimax_obc(akt_gleb+1, max_gleb, rev(kolor), True, best_ocena)
                        self.pl.wyjmij(j)

                    # jeśli nasza odpowiedź już jest lepsza niż nasze odpowiedzi
                    # przy poprzednich ruchach  przeciwnika, to nie ma co dalej
                    # analizować, bo przeciwnik i tak tego ruchu nie wybierze
                    if wyn < best_ocena_poprz:
                        return wyn

                    if wyn < best_ocena:
                        best_ocena = wyn
                
        return best_ocena

        
    # wykonuje każdy możliwy ruch danym kolorem,
    # oceniając go do zadanej głębokości i zwraca listę
    # z oceną każdego z nich
    def ocen_ruchy(self, plan: Plansza, kolor: Pole):

        self.pl = plan

        oceny = [None]*self.pl.n_col

        if kolor == Pole.zolty:
            czy_maks_gracz = True
            wygrana_punkty = 100
            brak_ruch_punkty = -float('inf')
        else:
            czy_maks_gracz = False
            wygrana_punkty = -100
            brak_ruch_punkty = float('inf')

        for j in range(self.pl.n_col):

            if self.pl.wrzuc(j, kolor):

                # sprawdzam, czy koniec
                wygrana = self.pl.czy_koniec()[0]
                if wygrana:
                    oceny[j] = wygrana_punkty
                else:
                    wyn = self.minimax(1, self.glebokosc_anal, rev(kolor), not czy_maks_gracz)
                    oceny[j] = wyn

                self.pl.wyjmij(j)
            else:
                oceny[j] = brak_ruch_punkty
        
        return oceny

    # wykonuje każdy możliwy ruch danym kolorem,
    # oceniając go do zadanej głębokości i zwraca listę
    # z oceną każdego z nich
    def ocen_ruchy_obc(self, kolor):

        oceny = [None]*self.pl.n_col

        if kolor == Pole.zolty:
            czy_maks_gracz = True
            wygrana_punkty = 1000
            brak_ruch_punkty = -float('inf')
            mnoznik = 1
        else:
            czy_maks_gracz = False
            wygrana_punkty = -1000
            brak_ruch_punkty = float('inf')
            mnoznik = -1

        best_ocena = -mnoznik*float('inf')

        # Obcinanie powoduje, że przy obecnej funkcji oceny najbardziej optymalnie
        # jest zaczynać od środkowych kolumn
        kolejnosc_ocen = [3,2,4,1,5,0,6]
        for j in kolejnosc_ocen:

            if self.pl.wrzuc(j, kolor):

                # sprawdzam, czy koniec
                wygrana = self.pl.czy_koniec()[0]
                if wygrana:
                    oceny[j] = wygrana_punkty
                else:
                    wyn = self.minimax_obc(1, self.glebokosc_anal, rev(kolor), not czy_maks_gracz, best_ocena)
                    oceny[j] = wyn

                    if mnoznik * wyn > mnoznik * best_ocena:
                        best_ocena = wyn        

                self.pl.wyjmij(j)
            else:
                oceny[j] = brak_ruch_punkty
        
        return oceny

    def start(self):
        
        while True:
            kolor = Pole.zolty
            self.pl.print()

            #odczytuje ruch gracza
            self.nr_ruchu += 1
            j = input()
            if j == 'e':
                return
            self.pl.wrzuc(int(j), kolor = Pole.czerwony)

            if self.pl.czy_koniec()[0]:
                print("Wygrana Czerwonych!")
                exit()

            #ruchy = ocen_ruchy(kolor, 4)
            self.nr_ruchu += 1
            ruchy = self.ocen_ruchy_obc(kolor)
            print(ruchy)
            # Wybieram najlpeszy ruch
            najlepsza_ocena = max(ruchy)
            najlepszy_ruch = ruchy.index(najlepsza_ocena)

            # Wykonuje najlepszy ruch
            self.pl.wrzuc(najlepszy_ruch, kolor)
            self.pl.print()

            if self.pl.czy_koniec()[0]:
                print("Wygrana Żółtych!")
                exit()


    # start()


    # self.pl.czysc()
    # Plansza[0][3] = Pole.zolty
    # Plansza[0][2] = Pole.czerwony

    # #Plansza[3][4] = Pole.czerwony
    # self.pl.print()

    # #print(ocen_ruchy(Pole.zolty, 5))

    # ocen_ruchy_obc
    # #p.wrzuc(3, Pole.zolty)
    # #minimax(1, 1, Pole.czerwony, False)
    # #p.wrzuc(3, Pole.zolty)
