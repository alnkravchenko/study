#include <iostream>
using std::cin;
using std::cout;
using std::endl;

int main() {
    float firstEl;
    float differ;
    int numberOfEl;
    float nextEl;

    cout << "Кравченко О.О. ІС-93 Лабораторна робота №1 Варіант 13"<<endl;

    cout << "Enter first element of the progression: ";
    cin >> firstEl;
    cout << "Enter difference of the progression: ";
    cin >> differ;
    cout << "Enter number of element: ";
    cin >> numberOfEl;

    if (numberOfEl == 1) {
        nextEl = firstEl;
    }
    else {
        for (int i = 0; i <= numberOfEl-2; i++) {
            nextEl = firstEl + differ;
            firstEl = nextEl;
        }
    }

    cout << numberOfEl << " number of arithmetical progression is " << nextEl;
    return 0;
}