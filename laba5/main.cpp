#include <iostream>
using namespace std;

int main() {
    cout << "Кравченко О.О. ІС-93 Лабораторна рoбота №5 Варіант 13" << endl;
    int firstNum, secondNum; // Variable initialization
    cout << "Enter number p: ";
    cin >> firstNum;
    cout << "Enter number q: " ;
    cin >> secondNum;
    int dividers [firstNum]; // Array with all needed dividers
    int k = 0;


    for(int divider = 1; divider <= firstNum; divider++){ // Loop for searching dividers
        if (firstNum % divider == 0 && secondNum % divider != 0 && divider % secondNum != 0) { // Conditions for divider of first number and for checking coprime numbers (divider and second number)
            dividers[k] = divider; // Add divider into list of all dividers
            k++;
        }
    }
    cout << "dividers = {"; // Printing all needed dividers
    for (int counter = 0; counter < k; counter++ ) {
        cout << dividers[counter] << " ";
    }
    cout << "}";

}
