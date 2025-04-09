#include <iostream>  // biblioteca de input e output

using namespace std;  // importa o namespace standard output

int main() {
    string name;
    int age;
    char sex;
    double height;

    cout << "New person" << endl;

    cout << "Enter name: ";
    cin >> name;

    cout << "Enter age: ";
    cin >> age;

    cout << "Enter height: ";
    cin >> height;

    cout << "Enter sex: ";
    cin >> sex;

    if (age >= 60){
        cout << "Optional vote for elder people" << endl;
    } else if (age >= 18) {
        cout << "Obligatory vote" << endl;
    } else if (age >= 16){
        cout << "Optional vote for teenagers" << endl;
    } else{
        cout << "Can't vote yet" << endl;
    }

    return 0;
}