#include <iostream>
using namespace std;

int main(){
    int totalDias;
    int valores[2];
    int total[3];

    valores[0] = 365;
    valores[1] = 30;
    
    cin >> totalDias;

    // using greedy algorithms
    int i = 0;
    while (i < 2){
        total[i] = 0;
        while (totalDias >= valores[i]){
            totalDias -= valores[i];
            total[i] += 1;
        }
        i += 1;
    }

    total[2] = totalDias;

    cout << total[0] << " ano(s)" << endl;
    cout << total[1] << " mes(es)" << endl;
    cout << total[2] << " dia(s)" << endl;


    return 0;
}