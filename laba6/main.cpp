#include <iostream>
#include <cmath>
using namespace std;

float maximum, result, firstNum, secondNum, number1, number2; // Variables initialization

void input(){ // Input 's' and 't'
    cout << "Enter number s: ";
    cin >> firstNum;
    cout << "Enter number t: ";
    cin >> secondNum;
}

float formula(float a, float b){ // Formula for h(a, b)
    return (a / (1 + pow(b, 2))) + (b / (1 + pow(a, 2))) - pow((a - b), 3);
}

void solution(){ // Main calculations
    number1 = pow(formula(firstNum - secondNum, firstNum * secondNum), 2); // First number for searching
    // max number
    number2 = pow(formula(firstNum - secondNum, firstNum * secondNum), 4); // Second number for searching max number
    printf("First number for comparing: %.4f\n", number1);
    printf("Second number for comparing: %.4f\n",  number2);

    if (number1 > number2) { // Searching max number
        maximum = number1;
    } else {
        maximum = number2;
    }
    printf("Max number: %.4f\n", maximum);

    result = formula(firstNum, secondNum) + maximum + formula(1, 1); // Our final formula
}

void output(){ // Output the result
    printf("Our result = %.4f", result);
}

int main(){
    cout << "Кравченко О.О. ІС-93 Лабораторна рoбота №6 Варіант 13" << endl;
    input();
    solution();
    output();
}
