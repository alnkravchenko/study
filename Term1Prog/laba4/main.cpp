#include <iostream>
using namespace std;

int main() {
    int iterCount; // Variable initialization
    float x = 1;
    float y = 1;
    float result = 0;

    cout << "Кравченко О.О. ІС-93 Лабораторна рoбота №4 Варіант 13"<< endl;
    cout << "Enter number of iterations: ";
    cin >> iterCount;

    for (int count = 0; count <= iterCount; count++) { // Loop with number of iterations
        result += x / (1 + abs(y)); // Our formula
        y += x; // Change y
        x *= 0.3; // Change x
    }
    printf("%.4f", result); // Final result
}
