#include "header.h"

// Таймер 

inline double get_time() {
    return std::chrono::duration_cast<std::chrono::microseconds>(
               std::chrono::steady_clock::now().time_since_epoch())
               .count() / 1e6;
}

// Функция заполняет subvector<int> capacity = n с заданной стратегией роста
// Если время > timeout_sec — прерывает и возвращает aborted=true

Time timed_fill(unsigned int n, int grow_type, double grow_param, double timeout_sec) {
    subvector<int> v;
    v.set_growth(grow_type, grow_param);
    double timer = 0.0;
    for (unsigned int i = 0; i < n; ++i) {
        double t0 = get_time();
        v.push_back(i);
        double t1 = get_time();
        timer += t1 - t0;
        if (timer > timeout_sec) {
            Time r{-1.0, true};
            return r;
        }
    }
    Time r{timer, false};
    return r;
}
