#include <iostream>
using namespace std;

int main(){
    int d;
    cin >> d;

    if ((d - 6) % 8 == 0){
        cout << "1" << endl;
    } else if ((d - 7) % 8 == 0){
        cout << "2" << endl;
    } else{
        cout << "3" << endl;
    }

    return 0;
}