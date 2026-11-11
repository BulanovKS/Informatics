#include "header.h"

const char* mode_names_3[3] = {"borrow", "copy_each", "copy_once"};

std::string strings_3[3][5];
Text        texts_3[3][5];
std::size_t lengths_3[3] = {15, 1023, 16383};

// Структура для хранения измерений

struct Counters {
    std::size_t calls;
    std::size_t copied_bytes;
    std::size_t current_extra;
    std::size_t peak_extra;

    Counters() : calls(0), copied_bytes(0),
                 current_extra(0), peak_extra(0) {}

    void call(std::size_t sz) {
        ++calls;
        current_extra += sz;
        if (current_extra > peak_extra) peak_extra = current_extra;
    }
    void release(std::size_t sz) { current_extra -= sz; }
    void copied(std::size_t bytes) { copied_bytes += bytes; }
};

// Подготовка входных данных в виде массивов структур

void prepare_inputs_3() {
    std::string text_in;
    text_input("text.txt", text_in);

    for (int id = 0; id < 3; ++id) {
        std::size_t L = lengths_3[id];
        for (int s = 0; s < 5; ++s) {
            std::string& str = strings_3[id][s];
            str.reserve(L);
            for (std::size_t i = L * s; i < L * (s + 1); ++i) { str.push_back((char)(text_in[i])); }
            texts_3[id][s].data = str.c_str();
            texts_3[id][s].size = L;
        }
    }
}

// Функция сравнения трех режимов работы

void run_one_group_3(int mode, Text source, int K, Counters& c, unsigned long long& result) {
    std::size_t L = source.size;

    if (mode == 0) {
        for (int i = 0; i < K; ++i) {
            Stats s = analyze(source);
            result += (unsigned long long)(s.checksum + s.words);
        }
    } else if (mode == 1) {
        for (int i = 0; i < K; ++i) {
            std::size_t calls_size = L + 1;
            c.call(calls_size);
            char* copy = clone_text(source);
            c.copied(L);
            Text t = {copy, L};
            Stats s = analyze(t);
            result += (unsigned long long)(s.checksum + s.words);
            delete[] copy;
            c.release(calls_size);
        }
    } else {
        std::size_t calls_size = L + 1;
        c.call(calls_size);
        c.copied(L);
        char* copy = clone_text(source);
        Text t = {copy, L};
        for (int i = 0; i < K; ++i) {
            Stats s = analyze(t);
            result += (unsigned long long)(s.checksum + s.words);
        }
        delete[] copy;
        c.release(calls_size);
    }
}

void task_3() {
    prepare_inputs_3();

    std::ofstream csv("B_memory_" + std::string(opt_level) + ".csv");
    csv << "length,repeats,uses,mode,allocations,copied_bytes,peak_extra_bytes\n";

    const int Ks[3] = {1, 10, 100};
    const int G = 10;

    for (int id = 0; id < 3; ++id) {
        std::size_t L = lengths_3[id];
        
        for (int s = 0; s < 3; ++s) {
            int K = Ks[s];

            for (int m = 0; m < 3; ++m) {
                Counters c;
                unsigned long long total_result = 0;

                for (int g = 0; g < G; ++g) {
                    run_one_group_3(m, texts_3[id][g % 5], K, c, total_result);
                }
                if (c.current_extra != 0) {
                    std::cout << "Warning: current_extra != 0: "
                              << c.current_extra << '\n';
                }

                csv << L << ',' << G << ',' << K << ',' << mode_names_3[m] << ','
                    << c.calls << ',' << c.copied_bytes << ','
                    << c.peak_extra << '\n';
            }
        }
    }

    csv.close();
}