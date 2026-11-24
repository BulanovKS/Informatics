#include "header.h"

// Исследование std::vector

void task0() {
        std::ofstream f("csv_task0.csv", std::ios::out);
        f << "size,capacity" << std::endl;

        std::vector<int> v;
        for (int i = 0; i < 1'000'000; ++i) {
            v.push_back(i);
            f << v.size() << "," << v.capacity() << std::endl;
        }
        f.close();
}