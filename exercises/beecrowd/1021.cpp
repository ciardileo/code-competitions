#include <iostream>
#include <iomanip>
#include <cmath>
using namespace std;

int main(){
    double valorOriginal;
    int valorCentavos;
    int notas[6] = {10000, 5000, 2000, 1000, 500, 200};
    int moedas[6] = {100, 50, 25, 10, 5, 1};

    cin >> valorOriginal;

    valorCentavos = round(valorOriginal * 100);
    
    cout << fixed << setprecision(2);
    cout << "NOTAS:" << endl;
    for (int i = 0; i < 6; i++){
        int qtd = valorCentavos / notas[i];
        valorCentavos %= notas[i];
        cout << qtd << " nota(s) de R$ " << notas[i] / 100.00 << endl;
    }

    cout << "MOEDAS:" << endl;
    for (int i = 0; i < 6; i++){
        int qtd = valorCentavos / moedas[i];
        valorCentavos %= moedas[i];
        cout << qtd << " moeda(s) de R$ " << moedas[i] / 100.0 << endl;
    }
    

    return 0;
}