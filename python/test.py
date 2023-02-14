from plansza import Plansza, Pole
from silnik import Silnik
from collections import namedtuple

# Pole_tuple = namedtuple("Pole_tuple", "pusty, zolty, czerwony")
# Pol = Pole_tuple(pusty=0, zolty=1, czerwony=2)

# print(Pol.czerwony == Pol.zolty)
# print(Pol.czerwony)
pl = Plansza()
pl.wrzuc(3, Pole.czerwony)
pl.wrzuc(3, Pole.zolty)
pl.wrzuc(4, Pole.czerwony)
pl.wrzuc(2, Pole.zolty)
pl.wrzuc(2, Pole.czerwony)
pl.wrzuc(3, Pole.zolty)
pl.wrzuc(2, Pole.czerwony)
pl.wrzuc(5, Pole.zolty)
pl.wrzuc(2, Pole.czerwony)
# pl.wrzuc(3, Pole.zolty)

s = Silnik(1)

pl.print()

wyn = s.najlepszy_ruch(pl, Pole.zolty)
# wyn = s.minimax_obc_v2(1, 2, Pole.zolty, False, -1000)
print(wyn)
# pl.wrzuc(2, Pole.czerwony)
print(pl.czy_konczacy_ruch(2))
print(pl.gdzie_ostatni(3))

# print(pl.hash_string2())
