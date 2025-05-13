#include <iostream>
#include <iomanip>
using namespace std;

int main(){
    int number, hours;
    double salaryPerHour, totalSalary;

    cin >> number >> hours >> salaryPerHour;

    cout << fixed << setprecision(2);
    cout << "NUMBER = " << number << endl;
    cout << "SALARY = U$ " << hours * salaryPerHour << endl;

    return 0;
}