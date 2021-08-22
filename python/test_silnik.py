import unittest
from plansza import Plansza
from plansza import Pole
from silnik import Silnik

class Test_silnik(unittest.TestCase):

    def test_ocen(self):

        plansza = Plansza()
        s = Silnik(3)

        plansza.czysc()

        # pusta plansza
        wyn = s.ocen(plansza)
        self.assertEqual(wyn, 0)

        # jeden krazek, ujemny bo czerwony
        plansza.czysc()
        plansza.plansza[0][2] = Pole.czerwony
        #plansza.print()
        self.assertEqual(s.ocen(plansza), -s.wagi_ocena[2])

        # symetryczne rostawienie po jednym krążku
        plansza.czysc()
        plansza.plansza[0][2] = Pole.zolty
        plansza.plansza[0][4] = Pole.czerwony
        self.assertAlmostEqual(s.ocen(plansza), 0.0044)

        #niesymetryczne rostawienie
        plansza.czysc()
        plansza.plansza[0][3] = Pole.zolty
        plansza.plansza[0][2] = Pole.czerwony
        #self.assertEqual(s.ocen(plansza), s.wagi_ocena[3]-s.wagi_ocena[2])
        self.assertAlmostEqual(s.ocen(plansza), 0.57)

    # czy dobrze ogarnia przypadki, jak w środku analizy drzewka nastąpi wygrana
    def test_wygrana_w_srodku(self):
        plansza = Plansza()
        s = Silnik(5)
        plansza.czysc()
        plansza.plansza[0][1] = Pole.czerwony
        plansza.plansza[0][2] = Pole.czerwony
        plansza.plansza[1][2] = Pole.czerwony
        plansza.plansza[2][3] = Pole.czerwony
        plansza.plansza[1][4] = Pole.czerwony
        plansza.plansza[1][1] = Pole.zolty
        plansza.plansza[0][3] = Pole.zolty
        plansza.plansza[1][3] = Pole.zolty
        plansza.plansza[3][3] = Pole.zolty
        plansza.plansza[0][4] = Pole.zolty

        plansza.plansza[2][4] = Pole.zolty
        plansza.print()

        ocz_wyn=[-100, -100, -100, -100, 2.0543000000000005, -100, -100]
        self.assertEqual(s.ocen_ruchy(plansza, Pole.zolty), ocz_wyn)

    # funkcja ocen_ruchy wrzucała wygrywający ruch do analizy, zamiast ocenić go na maksa
    def test_ruch_do_wygranej(self):
        plansza = Plansza()
        s = Silnik(3)

        plansza.czysc()
        plansza.plansza[0][1] = Pole.zolty
        plansza.plansza[0][2] = Pole.zolty
        plansza.plansza[0][3] = Pole.zolty
        plansza.plansza[1][2] = Pole.zolty
        plansza.plansza[2][4] = Pole.zolty
        plansza.plansza[3][1] = Pole.zolty
        plansza.plansza[3][2] = Pole.zolty
        plansza.plansza[3][4] = Pole.zolty
        plansza.plansza[4][2] = Pole.zolty
        plansza.plansza[0][0] = Pole.czerwony
        plansza.plansza[0][4] = Pole.czerwony
        plansza.plansza[0][5] = Pole.czerwony
        plansza.plansza[1][1] = Pole.czerwony
        plansza.plansza[1][3] = Pole.czerwony
        plansza.plansza[1][4] = Pole.czerwony
        plansza.plansza[2][1] = Pole.czerwony
        plansza.plansza[2][2] = Pole.czerwony
        plansza.plansza[2][3] = Pole.czerwony
        p.print()

        ocz_wyn=[-100, -100, -100, 100, -100, -100, -100]
        self.assertEqual(s.ocen_ruchy(plansza, Pole.zolty), ocz_wyn)


if __name__ == '__main__':
    unittest.main()

