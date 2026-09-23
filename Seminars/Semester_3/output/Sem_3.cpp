#include <iostream>

void swap(int & a, int & b){
    int tmp = a;
    a = b;
    b = tmp;
}

void bubble_sort(int array[], int n){
    for (int i = 0; i < n; i++){
        for (int j = 0; j < n - i - 1; j++){
            if (array[j] > array[j + 1]){
                swap(array[j], array[j + 1]);
            }
        }
    }
}

int main(){
    int my_array[10];

    for (int i = 0; i < 10; ++i){
        std::cin >> my_array[i];
    }

    bubble_sort(my_array, 10);

    for (int i = 0; i < 10; ++i){
        std::cout << my_array[i] << ' ';
    }
}