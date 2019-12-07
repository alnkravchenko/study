#include <iostream>
#include <cmath>
using namespace std;

int size;
int modificatedNumber = 0;
int amount = 0; // Amount of negative elements in array
int summary = 0; // Summary of negative numbers from array
float average = 0.0; // Average of negative numbers from array
int* array = new int [size];
int* modificatedArray = new int [size/2];

void input(){ // Inputs size of array C(n)
    cout << "Enter size of array C(n): ";
    cin >> size;
}

void creating_array(){ // Creates array with random integers
    srand(time(NULL));
    cout << "C(n) = [";
    for (int index = 0; index < size; index++){ // Loop for filling array with random integers from -100 to
        // 100
        array[index] = rand()%199-100;
        if (index+1 < size){ // Output created array
            cout << array[index] << ", ";
        } else
            cout << array[index] << "]" << endl;
    }
}

void solution(){ // Algorithm from the task
    for (int element = 0; element <= size; element++) { // Loop for searching negative numbers in array
        if (array[element] < 0) {
            summary += array[element];
            amount += 1; // Amount of negative elements in array
        }
    }
    average = fabs(summary / amount);
    cout << "Average of negative numbers: " << average << endl;

    for (int count = 0; count <= (size/2); count++){ // Loop with even indexes of array
        modificatedNumber = array[2*count] * average; // Formula from task
        modificatedArray[count] = modificatedNumber;
    }
}

void output(){ // Outputs the result
    cout << "F(n) = [";
    for (int count = 0; count <= (size/2); count++){
        if (count < (size/2)){
            cout << modificatedArray[count] << ", ";
        } else {
            cout << modificatedArray[count] << "]";
        }
    }
}

int main(){
    cout << "Кравченко О.О. ІС-93 Лабораторна рoбота №7 Варіант 13" << endl;
    input();
    creating_array();
    solution();
    output();
}
