#include "header.h"

// Сравнение стратегий между собой и с std::vector

void task1() {
    std::ofstream f("csv_task1.csv");
    f << "n,plus_10,plus_100,mul_1_5,mul_2,stdvector" << std::endl;

    bool skip_10 = false, skip_100 = false;

    for (unsigned int n = 0; n <= 50'000; n += 500) {
        double t_10 = -1.0, t_100 = -1.0;

        if (!skip_10) {
            Time r = timed_fill(n, 0, 10.0);
            t_10 = r.time_sec;
            if (r.aborted) {
                skip_10 = true;
                std::cout << "(+10 aborted) ";
            }
        }

        if (!skip_100) {
            Time r = timed_fill(n, 0, 100.0);
            t_100 = r.time_sec;
            if (r.aborted) {
                skip_100 = true;
                std::cout << "(+100 aborted) ";
            }
        }

        double t_15 = timed_fill(n, 1, 1.5).time_sec;
        double t_2 = timed_fill(n, 1, 2.0).time_sec;

        double t0 = get_time();
        {
            std::vector<int> sv;
            for (unsigned int i = 0; i < n; ++i) sv.push_back(i);
        }
        double t_std = get_time() - t0;

        f << n << "," << t_10 << "," << t_100 << ","
          << t_15 << "," << t_2 << "," << t_std << std::endl;
    }
    f.close();
}
