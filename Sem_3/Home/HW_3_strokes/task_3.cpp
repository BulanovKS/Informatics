#include "header.h"
#include <cstddef>
#include <string>
#include <fstream>
#include <iostream>

#ifdef __OPTIMIZE__
const char* g3_opt_level = "O2";
#else
const char* g3_opt_level = "O0";
#endif

volatile unsigned long long g3_sink = 0;

const char* g3_mode_names[3] = {"borrow", "copy_each", "copy_once"};

std::string g3_strings[3][5];
Text        g3_texts[3][5];
std::size_t g3_lengths[3] = {15, 1023, 16383};

struct Counters {
    std::size_t allocations;
    std::size_t copied_bytes;
    std::size_t current_extra;
    std::size_t peak_extra;
    Counters() : allocations(0), copied_bytes(0),
                 current_extra(0), peak_extra(0) {}
    void alloc(std::size_t sz) {
        ++allocations;
        current_extra += sz;
        if (current_extra > peak_extra) peak_extra = current_extra;
    }
    void release(std::size_t sz) { current_extra -= sz; }
    void copied(std::size_t bytes) { copied_bytes += bytes; }
};

void g3_prepare_inputs() {
    for (int idx = 0; idx < 3; ++idx) {
        std::size_t L = g3_lengths[idx];
        for (int s = 0; s < 5; ++s) {
            std::string& str = g3_strings[idx][s];
            str.reserve(L);
            for (std::size_t i = 0; i < L; ++i) {
                if (i % 10 == 0) str.push_back(' ');
                else if (i % 15 == 0) str.push_back('\t');
                else str.push_back((char)('a' + ((i + s) % 26)));
            }
            g3_texts[idx][s].data = str.c_str();
            g3_texts[idx][s].size = L;
        }
    }
}

void g3_run_one_group(int mode, Text source, int K,
                      Counters& c, unsigned long long& result) {
    std::size_t L = source.size;
    if (mode == 0) {
        for (int i = 0; i < K; ++i) {
            Stats s = analyze(source);
            result += (unsigned long long)(s.checksum + s.words);
        }
    } else if (mode == 1) {
        for (int i = 0; i < K; ++i) {
            std::size_t alloc_size = L + 1;
            c.alloc(alloc_size);
            char* copy = new char[alloc_size];
            c.copied(L);
            for (std::size_t j = 0; j < L; ++j) copy[j] = source.data[j];
            copy[L] = '\0';
            Text t = {copy, L};
            Stats s = analyze(t);
            result += (unsigned long long)(s.checksum + s.words);
            delete[] copy;
            c.release(alloc_size);
        }
    } else {
        std::size_t alloc_size = L + 1;
        c.alloc(alloc_size);
        char* copy = new char[alloc_size];
        c.copied(L);
        for (std::size_t j = 0; j < L; ++j) copy[j] = source.data[j];
        copy[L] = '\0';
        Text t = {copy, L};
        for (int i = 0; i < K; ++i) {
            Stats s = analyze(t);
            result += (unsigned long long)(s.checksum + s.words);
        }
        delete[] copy;
        c.release(alloc_size);
    }
}

void task_3() {
    g3_prepare_inputs();

    std::ofstream csv("experiment_B_memory.csv");
    csv << "length,repeats,uses,mode,allocations,copied_bytes,peak_extra_bytes\n";

    const int Ks[3] = {1, 10, 100};
    const int G = 10;

    for (int idx = 0; idx < 3; ++idx) {
        std::size_t L = g3_lengths[idx];
        for (int ki = 0; ki < 3; ++ki) {
            int K = Ks[ki];
            for (int m = 0; m < 3; ++m) {
                Counters c;
                unsigned long long total_result = 0;
                for (int g = 0; g < G; ++g) {
                    g3_run_one_group(m, g3_texts[idx][g % 5], K, c, total_result);
                }
                g3_sink += total_result;
                if (c.current_extra != 0) {
                    std::cerr << "Warning: current_extra != 0: "
                              << c.current_extra << '\n';
                }

                csv << L << ',' << G << ',' << K << ',' << g3_mode_names[m] << ','
                    << c.allocations << ',' << c.copied_bytes << ','
                    << c.peak_extra << '\n';

                std::size_t pred_alloc = 0, pred_copied = 0, pred_peak = 0;
                if (m == 1) {
                    pred_alloc = (std::size_t)G * K;
                    pred_copied = (std::size_t)G * K * L;
                    pred_peak = L + 1;
                } else if (m == 2) {
                    pred_alloc = (std::size_t)G;
                    pred_copied = (std::size_t)G * L;
                    pred_peak = L + 1;
                }
                std::cout << "L=" << L << " K=" << K
                          << " mode=" << g3_mode_names[m]
                          << " | alloc actual=" << c.allocations
                          << " pred=" << pred_alloc
                          << " | copied actual=" << c.copied_bytes
                          << " pred=" << pred_copied
                          << " | peak actual=" << c.peak_extra
                          << " pred=" << pred_peak << '\n';
            }
        }
    }

    csv.close();
    std::cout << "Experiment B (memory) done. Results in experiment_B_memory.csv\n";
}