#include "header.h"

void inf_cycle() {
    float x = 16777216.0f;
    float stop = 16777218.0f;

    std::cout << "start: " << x;

    while (x < stop) {
        x = x + 1.0f;
    }
    std::cout << "finish: " << x;
}