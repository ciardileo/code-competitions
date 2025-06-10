#include <iostream>
#include <iomanip>
#include <cmath>
using namespace std;

int main(){
    double radius, volume;
    const double PI = 3.14159;
    
    cin >> radius;
    
    cout << fixed << setprecision(3);
    volume = 4/3.0 * PI * pow(radius, 3);
    cout << "VOLUME = " << volume << endl;
    
    
    return 0;
}