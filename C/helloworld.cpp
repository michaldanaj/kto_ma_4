#include <iostream>
#include <vector>
#include <string>

using namespace std;

enum pole{
    puste = 0,
    zolty = 1,
    czerwony = 2
};

const int n_row=6;
const int n_col=7;

pole plansza[n_row][n_col];

void plansza_print(){
    cout << endl;
    cout << endl;

    for (int j=0; j < n_col; j++)
        cout << " " << j+1;
    cout << endl;
    
    for (int i=n_row-1; i >= 0 ; i--){
        cout << "|";
        for (int j=0; j < n_col ; j++){
            if (plansza[i][j] == puste)
                cout << ' ';
            else if (plansza[i][j] == zolty)
                cout << 'Z';
            else if (plansza[i][j] == czerwony)
                cout << 'C';
            cout << "|";
        }
        cout << endl;
    }

    for (int j=0; j < n_col*2+1; j++)
        cout << "=";
    cout << endl;
}

// Wrzuca w j-tą kolumnę klocek o kolorze kolor
void wrzuc(int j, pole kolor){
    int i=0;
    while (plansza[i][j] != puste && i < n_row)
        i++;
    
    if (i < n_row)
        plansza[i][j] = kolor;
}

//Ocena z punktu widzenia żółtego
double ocen_plansze(){
    double punkty = 0;

    //punkty za centrum
    for (int i=0; i < n_row; i++)
        for (int j=0; j< n_col; j++){
            double punkt;
            punkt = j % 3 + 1;
            if (plansza[i][j] == zolty)
                punkty += punkt;
            else if (plansza[i][j] == czerwony)
                punkty -= punkt;
        }

    //punkty za sekwencje
    //ocena polega na zliczeniu ile w sumie jest w danej linii
    //jest danych żetonów ciągiem, w każdą stronę od danego pola
    //ocena pola powinna być osobna dla każdego koloru

    return (punkty);
}

//Ocena z punktu widzenia żółtego
bool czy_koniec(){
    bool koniec = false;
    int ile_zoltych, ile_zielonych;

    //idę poziomo
    for (int i=0; i < n_row; i++){
        ile_zoltych = 0;
        ile_zielonych = 0;
        for (int j=0; j< n_col; j++){
            if (plansza[i][j] == zolty){
                ile_zoltych++;
                ile_zielonych = 0;
            }
            else if (plansza[i][j] == czerwony){
                ile_zoltych = 0;
                ile_zielonych ++;
            }
            else {
                ile_zoltych = 0;
                ile_zielonych = 0;
            }
        }
    }

    //idę pionowo
    for (int j=0; j< n_col; j++){
        ile_zoltych = 0;
        ile_zielonych = 0;
        for (int i=0; i < n_row; i++){
            if (plansza[i][j] == zolty){
                ile_zoltych++;
                ile_zielonych = 0;
            }
            else if (plansza[i][j] == czerwony){
                ile_zoltych = 0;
                ile_zielonych ++;
            }
            else {
                ile_zoltych = 0;
                ile_zielonych = 0;
            }
        }
    }
    
    return true;
}



int main()
{
    int gdzie=9;
    cout << "Żeby skończyć, wpis 0." << endl;
    plansza_print();
    while (gdzie != 0){
        cout << "Podaj gdzie postawić" << endl;
        cin >> gdzie;
        wrzuc(gdzie-1, zolty);
        plansza_print();
    }
}

