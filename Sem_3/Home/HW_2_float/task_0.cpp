#include "header.h"

void int_bin(unsigned int N) {
    for (int i = 31; i >= 0; --i) {
        std::cout << ((N >> i) & 1);
    }
    std::cout << std::endl;
}