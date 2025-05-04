#include <iostream>
#include <cmath>
#include <iomanip>
using namespace std;

int main(){
    float x1, x2, y1, y2;
    cin >> x1;
    cin >> y1;
    cin >> x2;
    cin >> y2;

    float distance = sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2));  // imported with (cmath)

    cout << fixed << setprecision(4);  // sets the decimal precision to 4 (imported with iomanip)
    cout << distance << endl;

    return 0;
}