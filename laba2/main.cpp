#include <iostream>
#include <cmath>
using namespace std;

int main() {
    float koord1; // It's x
    float koord2; // It's y
    bool flag1 = false; // For square
    bool flag2 = false; // For circle

    cout << "Кравченко О.О. ІС-93 Лабораторна рoбота №2 Варіант 13" << endl;

    cout << "Enter first coordinate: ";
    cin >> koord1;
    cout << "Enter second coordinate: ";
    cin >> koord2;

    if ((koord1 > -1 and koord1 < 1) or koord1 == -1 or koord1 == 1){ // Conditions for circle x^2 + y^2 = 4
        if (pow((koord1 - 1), 2) + pow(koord2, 2) <= 4.0) {
            flag2 = true;
        }
    } else if ((koord1 > 1 and koord1 < 3) or koord1 == 3 or koord1 == 1) { // Conditions for square |x| + |y| = 2
        if ((abs(koord1) - 1) + abs(koord2) <= 2.0) {
            flag1 = true;
        }
    }

    if (flag1 or flag2) {
        cout << "x,y belong to the area";
    } else {
        cout << "x,y don`t belong to the area";
    }
}
