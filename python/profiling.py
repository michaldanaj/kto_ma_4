from plansza import Plansza, Pole
from silnik import Silnik
import cProfile

pl = Plansza()
pl.wrzuc(3, Pole.zolty)

silnik = Silnik(7)
cProfile.run("silnik.najlepszy_ruch(pl, Pole.czerwony)")
