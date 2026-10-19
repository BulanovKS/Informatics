#include "header.h"

union Number{
    float f;
    unsigned int ui;
};

void float_bin(float N) {
    Number num;
    num.f = N;
    int_bin(num.ui);    
}
