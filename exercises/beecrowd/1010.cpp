#include <iostream>
#include <iomanip>
using namespace std;

int main(){
    int cod1, cod2, qtd1, qtd2;
    double valor1, valor2, valorTotal;

    cin >> cod1 >> qtd1 >> valor1;
    cin >> cod2 >> qtd2 >> valor2;

    valorTotal = qtd1 * valor1 + qtd2 * valor2;

    cout << fixed << setprecision(2);
    cout << "VALOR A PAGAR: R$ " << valorTotal << endl;

    return 0;
}