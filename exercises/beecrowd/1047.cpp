#include <iostream>
using namespace std;

/*
7:45
10:30
2 45 

8:30
9:45
1 15

8:40
8:49
0 9

8:40
6:39
9 59 

7:15
6:10

1. subtrair as horas
2. subtrair o horario final do inicial, se o resultado for negativo, diminui 1 das horas e subtrai esse valor de 60, sendo os minutos atuais
3. se a hora final for menor que a inicial, ou a hora for igual e o minuto final for menor, quer dizer que se passaram 24 horas - (diferença entre as horas).
*/

int main(){
    int horaInicial, minutoInicial, horaFinal, minutoFinal, duracaoHoras, duracaoMinutos;

    cin >> horaInicial >> minutoInicial >> horaFinal >> minutoFinal;

    if ((horaFinal < horaInicial) || ((horaFinal == horaInicial) && (minutoFinal <= minutoInicial))){  // passo 3
        duracaoHoras = 24 - abs(horaFinal - horaInicial);
       
    } else{
        duracaoHoras = horaFinal - horaInicial;
    }

    duracaoMinutos = minutoFinal - minutoInicial;

    if (duracaoMinutos < 0){
        duracaoHoras -= 1;
        duracaoMinutos = 60 - abs(duracaoMinutos);
    }

    cout << "O JOGO DUROU " << duracaoHoras << " HORA(S) E " << duracaoMinutos << " MINUTO(S)" << endl;

    return 0;
}