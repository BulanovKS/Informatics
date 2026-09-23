#include "utility.hpp"

void swap(int & a, int & b){
    int tmp = a;
    a = b;
    b = tmp;
}

bool is_sorted(int array[], int n){
    for (int i = 0; i < n-1; i++){
        if (array[i+1] < array[i]){
            return false;
        }
    }
    return true;
}