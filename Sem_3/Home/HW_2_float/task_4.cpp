#include "header.h"

// Ряд Лейбница: pi/4 = 1 - 1/3 + 1/5 - 1/7 + ...

float leibniz(int n) {
    float sum = 0.0;
    int sign = 1;

    for (int k = 0; k < n; ++k) {
        sum += sign / (2.0 * k + 1.0);
        sign = -sign;
    }
    return 4.0 * sum;
}

// Ряд Нилаканты: pi = 3 + 4/(2*3*4) - 4/(4*5*6) + 4/(6*7*8) - ...

float nilakantha(int n) {
    float sum = 3.0;
    int sign = 1;

    for (int k = 1; k <= n; ++k) {
        float summand = (2.0 * k) * (2.0 * k + 1.0) * (2.0 * k + 2.0);
        sum += sign * 4.0 / summand;
        sign = -sign;
    }
    return sum;
}

// Формула Валлиса:  pi/2 = (2/1)*(2/3)*(4/3)*(4/5)*(6/5)*(6/7)*...
float wallis(int n) {
    float product = 1.0;

    for (int k = 1; k <= n; ++k) {
        float p = 2.0 * k;
        product *= (p * p) / ((p - 1.0) * (p + 1.0));
    }
    return 2.0 * product;
}

// Формула Бэйли-Боруэйна-Плаффа (Bailey-Borwein-Plouffe): pi = sum_{k=0}^inf 1/16^k * { 4/(8k+1) - 2/(8k+4) - 1/(8k+5) - 1/(8k+6)}
float BBP(int n) {
    float sum = 0.0;

    for (int k = 0; k < n; ++k) {
        float summand = (4.0 / (8.0 * k + 1.0) - 2.0 / (8.0 * k + 4.0) - 1.0 / (8.0 * k + 5.0) - 1.0 / (8.0 * k + 6.0)) / float(pow(16.0, k));
        sum += summand;
    }
    return sum;
}

// pi = 6 * sqrt(3) * sum_{k=1}^inf (-1)^(n + 1) / (3^n * (2n - 1))

float untitled(int n) {
    float sum = 0.0;
    int sign = 1;

    for (int k = 1; k <= n; ++k) {

        float summand = sign / (float(pow(3.0, k)) * (2.0 * k - 1.0));
        sum += summand;
        sign = -sign;
    }
    return 6.0 * float(sqrt(3)) * sum;
}

float pi_error(float num) {
    float pi = 3.141592653589793;
    float error = num - pi;
    return error;
}

void pi_terminal(int n) {
    std::cout << "кол-во итераций: " << n << std::endl;
    std::cout << "Ошибка Лейбница: " << pi_error(leibniz(n)) << std::endl;
    std::cout << "Ошибка Нилаканты: " << pi_error(nilakantha(n)) << std::endl;
    std::cout << "Ошибка Валлиса: " << pi_error(wallis(n)) << std::endl;
    std::cout << "Ошибка Бэйли-Боруэйна-Плаффа: " << pi_error(BBP(n)) << std::endl;
    std::cout << "Ошибка безымянной: " << pi_error(untitled(n)) << std::endl;
}

void pi_csv(int n, std::ofstream& file) {
    file << n << "," << leibniz(n) << "," << nilakantha(n) << "," << wallis(n) << "," << BBP(n) << "," << untitled(n) << std::endl;
}

void pi(int start, int end) {
    std::ofstream f("pi_csv.csv", std::ios::out);
    f << "кол-во итераций," << "Лейбниц," << "Нилакант," <<  "Валлис," << "Бэйли-Боруэйн-Плафф," << "Безымянная," << std::endl;

    for (int i = start; i <= end; i += 1) {
        pi_terminal(i);
        pi_csv(i, f);
    }
}