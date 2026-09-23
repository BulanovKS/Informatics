#include <iostream>
#include <chrono>
#include "functions.hpp"

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
    int my_array[100000];

    for (int n = 100; n < 100000; n *= 10){
        double result_time = 0;
        int K = 10;
        for (int k = 0; k < K; k++){
            for (int i = 0; i < n; ++i){
                my_array[i] = n - i;
        }
            auto t1 = std::chrono::steady_clock::now();

            bubble_sort(my_array, n);

            auto t2 = std::chrono::steady_clock::now();

            result_time += std::chrono::duration<double>(t2-t1).count();
        }
        std::cout << n << ": Time: " << result_time / double(K) << '\n';
    }

}