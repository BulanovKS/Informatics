#include "header.h"

const char* mode_names_3[3] = {"borrow", "copy_each", "copy_once"};

std::size_t lengths_3[3] = {15, 1023, 16383};

void task_3() {
    std::ofstream csv("B_memory_predicts_" + std::string(opt_level) + ".csv");
    csv << "length,repeats,uses,mode,allocations,copied_bytes,peak_extra_bytes\n";

    const int Ks[3] = {1, 10, 100};
    const int G = 10;

    for (int id = 0; id < 3; ++id) {
        std::size_t L = lengths_3[id];
        
        for (int s = 0; s < 3; ++s) {
            int K = Ks[s];

            for (int m = 0; m < 3; ++m) {
                std::size_t pred_calls = 0, pred_copied = 0, pred_peak = 0;

                if (m == 1) {
                    pred_calls = (std::size_t)G * K;
                    pred_copied = (std::size_t)G * K * L;
                    pred_peak = L + 1;
                } else if (m == 2) {
                    pred_calls = (std::size_t)G;
                    pred_copied = (std::size_t)G * L;
                    pred_peak = L + 1;
                }

                csv << L << ',' << G << ',' << K << ',' << mode_names_3[m] << ','
                    << pred_calls << ',' << pred_copied << ','
                    << pred_peak << '\n';
            }
        }
    }

    csv.close();
}