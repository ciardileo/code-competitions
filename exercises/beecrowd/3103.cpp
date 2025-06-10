#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
using namespace std;

/*
Pegar o número e ordená-lo em ordem crescente
Caso houver um 0 no começo, percorrer as letras até encontrar o primeiro número não nulo e trocar com este
*/

int main(){
    int n;
    string numero;
    vector<string> respostas;

    cin >> n;

    for (int i = 0; i < n; i++){
        cin >> numero;
        sort(numero.begin(), numero.end());
        
        if (numero[0] == '0'){
            for (int j = 0; j < numero.size(); j++){
                if (numero[j] != '0'){
                    swap(numero[0], numero[j]);
                    break;
                }
            }
        }

        respostas.push_back(numero);
    }

    for (int i = 0; i < respostas.size(); i++){
        cout << respostas[i] << endl;
    }

    return 0;
}