#include <iostream>
#include <cmath>
#include <iomanip>
using namespace std;

int main(){
    double radius;
    const double pi = 3.14159;

    cin >> radius;

    double area = pi * pow(radius, 2);
    cout << fixed << setprecision(4);
    cout << "A=" << area << endl;

    return 0;
}