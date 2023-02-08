from silnik import Silnik
from plansza import Plansza
from plansza import Pole
from plansza import rev
import logging as log

pl = Plansza()
ruchy:list[int] = []

class Czlowiek:

    def pobierz_ruch(self, plansza:Plansza, kolor: Pole) -> str: 
        #odczytuje ruch gracza
        return input()

class Komp:
    def __init__(self):
       self.s = Silnik(6) 

    def pobierz_ruch(self, plansza:Plansza, kolor: Pole) -> int:
        return self.s.najlepszy_ruch(plansza, kolor)

def zamien_ruch(czyj_ruch: str):
    if czyj_ruch=='czlowiek':
        return 'komp'
    else:
        return 'czlowiek'


log.basicConfig(filename='log_gra.log', filemode='a', format='%(asctime)s - %(levelname)s - %(message)s',
    level=log.DEBUG, datefmt='%d-%b-%y %H:%M:%S')
log.info("NOWA GRA")
gracze = [ Komp(), Czlowiek()]
czyj_ruch_idx = 0
kolor = Pole.czerwony
while True:

    zawodnik = gracze[czyj_ruch_idx]

    pl.print()

    j = zawodnik.pobierz_ruch(pl, kolor)    
    if isinstance(j, str):
        if j == 'e':
            break
        j = int(j)

    ruchy.append(j)
    pl.wrzuc(j, kolor)
    pl.print()

    if pl.czy_koniec()[0]:
        print("Wygrana!")
        break

    kolor = rev(kolor)
    #czyj_ruch = zamien_ruch(czyj_ruch)
    czyj_ruch_idx = 1 - czyj_ruch_idx
log.info('wpis do loga')
log.info(ruchy)
log.info('\n')
log.info(pl)