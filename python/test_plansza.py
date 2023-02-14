import unittest
from plansza import Plansza
from plansza import Pole

# from silnik import Silnik


class Testp(unittest.TestCase):
    def test_czy_koniec(self):
        p = Plansza()

        # wypełnienie bez  wygranej
        p.wypelnij()
        self.assertEqual(p.czy_koniec()[0], False)
        self.assertEqual(p.czy_wygrany_ruch(0, 0), False)
        self.assertEqual(p.czy_wygrany_ruch(0, 4), False)
        self.assertEqual(p.czy_wygrany_ruch(4, 0), False)
        self.assertEqual(p.czy_wygrany_ruch(4, 4), False)

        # pozioma na dole
        p.wypelnij()
        p.plansza[0][0] = Pole.czerwony
        p.plansza[0][1] = Pole.czerwony
        p.plansza[0][2] = Pole.czerwony
        p.plansza[0][3] = Pole.czerwony
        # p.print()
        self.assertEqual(p.czy_koniec()[0], True)
        self.assertEqual(p.czy_wygrany_ruch(0, 3), True)
        self.assertEqual(p.czy_wygrany_ruch(0, 1), True)

        # pozioma prawy górny róg
        p.wypelnij()
        p.plansza[5][3] = Pole.czerwony
        p.plansza[5][4] = Pole.czerwony
        p.plansza[5][5] = Pole.czerwony
        p.plansza[5][6] = Pole.czerwony
        p.print()
        self.assertEqual(p.czy_koniec()[0], True)
        self.assertEqual(p.czy_wygrany_ruch(5, 6), True)
        self.assertEqual(p.czy_wygrany_ruch(5, 3), True)

        # pionowo
        p.wypelnij()
        p.plansza[2][5] = Pole.zolty
        p.plansza[3][5] = Pole.zolty
        p.plansza[4][5] = Pole.zolty
        p.plansza[5][5] = Pole.zolty
        # p.print()
        self.assertEqual(p.czy_koniec()[0], True)
        self.assertEqual(p.czy_wygrany_ruch(2, 5), True)

        # w prawo góra
        p.wypelnij()
        p.plansza[1][2] = Pole.zolty
        p.plansza[2][3] = Pole.zolty
        p.plansza[3][4] = Pole.zolty
        p.plansza[4][5] = Pole.zolty
        # p.print()
        self.assertEqual(p.czy_koniec()[0], True)
        self.assertEqual(p.czy_wygrany_ruch(1, 2), True)
        self.assertEqual(p.czy_wygrany_ruch(2, 3), True)
        self.assertEqual(p.czy_wygrany_ruch(4, 5), True)
        self.assertEqual(p.czy_wygrany_ruch(1, 0), False)

        # w prawo góra
        p.wypelnij()
        p.plansza[2][0] = Pole.zolty
        p.plansza[3][1] = Pole.zolty
        p.plansza[4][2] = Pole.zolty
        p.plansza[5][3] = Pole.zolty
        # p.print()
        self.assertEqual(p.czy_koniec()[0], True)
        self.assertEqual(p.czy_wygrany_ruch(5, 3), True)
        self.assertEqual(p.czy_wygrany_ruch(0, 6), False)
        self.assertEqual(p.czy_wygrany_ruch(5, 2), False)

        # w prawo dół
        p.wypelnij()
        p.plansza[5][0] = Pole.zolty
        p.plansza[4][1] = Pole.zolty
        p.plansza[3][2] = Pole.zolty
        p.plansza[2][3] = Pole.zolty
        # p.print()
        self.assertEqual(p.czy_koniec()[0], True)
        self.assertEqual(p.czy_wygrany_ruch(5, 0), True)
        self.assertEqual(p.czy_wygrany_ruch(0, 6), False)
        self.assertEqual(p.czy_wygrany_ruch(5, 2), False)

    def test_hash(self):
        p = Plansza()
        p.wypelnij()
        hash = p.hash_string()
        print(hash)


if __name__ == "__main__":
    unittest.main()
