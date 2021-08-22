Pole wiekości 6 w pionie i 7 w poziomie





Ocena planszy:

- **Ocena zakończenia.** Na start +100 za wygraną, -100 za przegraną, 0 z nierozstrzygnięte

- Bardziej istotne jest centrum niż  boki  - **ocena rozstawienia**

  Zakładam, że lepiej jest mieć jeden krążek w centrum i w drugiej kolumnie od centrum, niż dwa w pierwszej od centrum. Przykładowe wagi od centrum (1), do skraju (4):
  $$
  (4-x)^2/9
  $$
  1, 0.44, 0.11, 0

  Oceniam jednego i drugiego i odejmuję, ale uwzględniając inicjatywę (następny punkt).

- Zakładam, że rozpoczynający (żółty) jest w inicjatywie, dlatego promuję jego pozycję. Ma to zapobiec takiej sytuacji, że jak ocena jest robiona dla symetrycznych pozycji, np. krążki w skrajnych kolumnach, to ocena byłaby taka sama jak by były w kolumnie o jedną bliżej środka. A chcę promować pozycje skupione w środku, dlatego muszę je jakoś zróżnicować. Dlatego ocenę rozstawienia rozpoczynającego mnożę o 0.01 przed odjęciem.

- Trzeba by było jednak dodać jeszcze jakieś punkty, żeby nie rosła wieża w górę, a w poziomie się rozwijał. Czyli chcemy stawiać w  centrum, o ile nie może zejść z poziomem niżej i postawić blisko centrum. Może też wagi dać za wysokość

- Albo jakieś dodatkowe punkty za 'pootwieranie' linii

Wybór ruch

* A co jeśli jest kilka ruchów z taką samą punktacją? Losowo przecież.

Może coś takiego jak dynamiczne punkty przypisywane do pola? Albo jakiś mnożnik do standardowego przydziału punktów? Przykładu:

* Jeśli pole jest wolne, a później trzy w rzędzie, to maks punktów
* Jeśli pole jest wolne, później trzy w rzędzie, a później wolne, to maks punktów
* Jeśli w jakieś pole wchodzą dwa układy, to sumowane są punkty z obu i mnożone przez jakąś premię
* Jeśli na polu są punkty za jakiś układ, i powyżej również, to każde z tych pól dostaje jakąś premię

