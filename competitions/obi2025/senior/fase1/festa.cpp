#include <iostream>
#include <algorithm>
#include <cmath>
using namespace std;

int main() {
    int E, S, L;
    cin >> E >> S >> L;
    
    // se supermercado e lojinha estiverem do mesmo lado
    if ((S <= E && L <= E) || (S >= E && L >= E)) {
        // a distância do mais longe * 2
        cout << (max(abs(S - E), abs(L - E)) * 2) << endl;
    } else {
        int distancia = abs(S - E) * 2 + abs(L - E) * 2;
        cout << distancia << endl;
    }

    return 0;
}