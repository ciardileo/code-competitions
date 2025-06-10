#include <iostream>
#include <iomanip>
#include <string>
using namespace std;

int main(){
    string nome;
    double salarioFixo, totalVendas, totalSalario;

    cin >> nome >> salarioFixo >> totalVendas;

    totalSalario = salarioFixo + 0.15 * totalVendas;
    cout << fixed << setprecision(2);
    cout << "TOTAL = R$ " << totalSalario << endl;

    return 0;
}