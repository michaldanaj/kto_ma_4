Chciałbym osiągnąć dwie rzeczy
1. Nieocenianie pozycji na planszy, która już w tym wywyołaniu algorytmu
   została oceniona, a powstała w innej sekwencji ruchów, np pierwsza
   pozycja z ruchów 3,2,4, a druga z 4,2,3.
2. Może zapamiętanie wszystkich stanów poprzedniego wywołania algorytmu,
   tak aby nie trzeba było znów przechodzić wszystkich głębokości, a tylko
   dołożyć nową głębokość.

Myślę że można to zrealizować następująco.
Powstaje jedna struktura - hash mapa, gdzie kluczem jest pozycja, a wartością
wartość oceny. Dodatkowo powinna się tu znaleźć informacja, jak głęboko 
względem ocenionej pozycji została dokonanan ocena. Jest to potrzebne, żeby
algorytm wiedział czy ocena powstała na tej głębokości na której on tearz 
się znajduje, dzięki czemu będzie wiedział czy uaktualniać ocenę pozycji,
czy wziąć zapisaną. 

Dodatkowym miejscem, w którym moglibyśmy wykorzystać te informacje, jest
kolejność analizowanych ruchów. Ze względu na wykorzystanie algorytmu minimax
z obcinaniem, najlepiej jest wykonywać na początku ruch dla którego jest
najwyższe prawdopodobnieństwo, że będzie najlepszym ruchem. Dzięki temu
kolejne, słabsze ruchy, mogą zostać szybko odcięte.

Druga struktura byłaby strukturą drzewiastą i przechowywałaby drzewo 
możliwych, przeanalizowanych ruchów. Struktura drzewiasta byłaby dogodna
z tego powodu, że w momencie wykonania ruchu, 6 gałęzi z najwyższego
poziomu posotaje zbędnych i powinny został w prosty sposób odcięte.
W węzłach drzewa powinno być wskazanie na konkretną pozycję z poprzedniej
struktury, dzięki czemu moglibyśmy odczytać wartość oceny dla tej pozycji.

Powinny tu również być wszystkie informacje potrzebne do odtworzenia stanu
algorytmu jaki był na moment analizy danej pozycji z drzewa, żeby móc
kontynuować wyliczenia od tego miejsca.

Takie podejście pozwoliłoby pogłębiać analizy, np. gdy wystarczająco dużo
czasu pozostało do wykonania analiz.
