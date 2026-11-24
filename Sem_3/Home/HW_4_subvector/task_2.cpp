#include "header.h"

// Зависимость времени от множителя capacity

void task2a() {
    std::ofstream f("csv_task2a.csv");
    f << "multiplier,time" << std::endl;

    const unsigned int n = 1'000'000;
    double multipliers[] = {1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0, 2.1, 2.2, 2.3, 2.4, 2.5, 3.0, 4.0};

    for (double m : multipliers) {
        Time r = timed_fill(n, 1, m);
        f << m << "," << r.time_sec << std::endl;
    }
    f.close();
}

// Зависимость времени от увеличения capacity на константу

void task2b() {
    std::ofstream f("csv_task2b.csv");
    f << "additive,time" << std::endl;

    const unsigned int n = 1'000'000;
    unsigned int adds[] = {10, 50, 100, 500, 1000, 5000, 10000, 50000, 100000, 500000};

    for (unsigned int a : adds) {
        Time r = timed_fill(n, 0, a);
        f << a << "," << r.time_sec << std::endl;
    }
    f.close();
}