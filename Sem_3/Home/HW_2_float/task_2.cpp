#include "header.h"

void overflow_mantissa(int N) {
std::cout << std::fixed;
std::cout.precision(2);

    for (int i = 0; i < N; i++){
        float numbers = pow(10.0f, i);
        std::cout << i << " " << numbers << " ";
        float_bin(numbers);
        std::cout << std::endl;
    } 
}