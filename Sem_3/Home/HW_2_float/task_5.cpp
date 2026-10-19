#include "header.h"

double time() { 
        return std::chrono::duration_cast<std::chrono::microseconds> (std::chrono::steady_clock::now().time_since_epoch()).count()/1e6; 
    }

double pi_time(float (func)(int n), int a) {
    float pi = 3.141592653589793;
    float accuracy = pow(10.0, -a);
    float error = 1.0;
    int n = 0;
    double t1 = 0.0;
    double t2 = 0.0;

    while (error > accuracy){
        n += 1;
        t1 = time();
        for (int i = 0; i < 1000000; i++){
        func(n);
        }
        t2 = time();
        float A = func(n);
        error = pi_error(A);
    }
    return double((t2 - t1));
}

void pi_time_terminal(int a) {
    std::cout << "Точность: " << a << " знаков после запятой" << std::endl;
    std::cout << "Время Лейбница: " << pi_time(leibniz, a) << std::endl;
    std::cout << "Время Нилаканты: " << pi_time(nilakantha, a) << std::endl;
    std::cout << "Время Валлиса: " << pi_time(wallis, a) << std::endl;
    std::cout << "Время Бэйли-Боруэйна-Плаффа: " << pi_time(BBP, a) << std::endl;
    std::cout << "Время безымянной: " << pi_time(untitled, a) << std::endl;
}

void pi_time_csv(int a, std::ofstream& file) {
    file << a << "," << pi_time(leibniz, a) << "," << pi_time(nilakantha, a) << "," << pi_time(wallis, a) << "," << pi_time(BBP, a) << "," << pi_time(untitled, a) << std::endl;
}

void pi_time_output(int a) {
    std::ofstream f("pi_time_csv.csv", std::ios::out);
    f << "Точность," << "Лейбниц," << "Нилакант," <<  "Валлис," << "Бэйли-Боруэйн-Плафф," << "Безымянная," << std::endl;

    for (int j = 1; j <= a; j += 1) {
        pi_time_terminal(j);
        pi_time_csv(j, f);
    }
}