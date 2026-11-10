#include "header.h"

const char* mode_names[3] = {"borrow", "copy_each", "copy_once"};
const int   perms[6][3] = {{0,1,2},{0,2,1},{1,0,2},{1,2,0},{2,0,1},{2,1,0}};

std::string strings[3][5];
Text        texts[3][5];
std::size_t lengths[3] = {15, 1023, 16383};

// Подготовка входных данных в виде массивов структур

void prepare_inputs() {
    std::string text_in;
    text_input("text.txt", text_in);

    for (int id = 0; id < 3; ++id) {
        std::size_t L = lengths[id];
        for (int s = 0; s < 5; ++s) {
            std::string& str = strings[id][s];
            str.reserve(L);
            for (std::size_t i = L * s; i < L * (s + 1); ++i) { str.push_back((char)(text_in[i])); }
            texts[id][s].data = str.c_str();
            texts[id][s].size = L;
        }
    }
}

// Функция копирования Text

char* clone_text(Text text) {
    char* copy = new char[text.size + 1];
    for (std::size_t i = 0; i < text.size; ++i) copy[i] = text.data[i];
    copy[text.size] = '\0';
    return copy;
}

// Функция сравнения трех режимов работы

void run_one_group(int mode, Text source, int K, unsigned long long& result) {
    std::size_t L = source.size;

    if (mode == 0) {
        for (int i = 0; i < K; ++i) {
            Stats s = analyze(source);
            result += (unsigned long long)(s.checksum + s.words);
        }

    } else if (mode == 1) {
        for (int i = 0; i < K; ++i) {
            char* copy = clone_text(source);
            Text t = {copy, L};
            Stats s = analyze(t);
            result += (unsigned long long)(s.checksum + s.words);
            delete[] copy;
        }

    } else {
        char* copy = clone_text(source);
        Text t = {copy, L};
        for (int i = 0; i < K; ++i) {
            Stats s = analyze(t);
            result += (unsigned long long)(s.checksum + s.words);
        }
        delete[] copy;
    }
}

double time_group(int mode, int id, int K, int G, unsigned long long& result) {
    unsigned long long local = 0;
    double total_time = 0;
    for (int g = 0; g < G; ++g) {
        auto start = std::chrono::steady_clock::now();
        run_one_group(mode, texts[id][g % 5], K, local);
        auto end = std::chrono::steady_clock::now();
        total_time += std::chrono::duration<double>(end - start).count();
    }
    result = local;
    return total_time;
}

int calibrate(int id, int K) {
    unsigned long long trash = 0;

    double t[3];
    for (int m = 0; m < 3; ++m) t[m] = time_group(m, id, K, 1, trash);

    double t_min = t[0];
    if (t[1] < t_min) t_min = t[1];
    if (t[2] < t_min) t_min = t[2];
    if (t_min <= 0.0) return 1;

    int G = (int)(0.1 / t_min);
    if (G < 1) G = 1;
    if (G > 10'000'000) G = 10'000'000;
    return G;
}

void task_2() {
    prepare_inputs();

    std::ofstream csv("B_" + std::string(opt_level) + ".csv");
    csv.precision(17);
    csv << "experiment,length,mode,work,repeats,uses,opt,trial,seconds,result\n";

    int Ks[3] = {1, 10, 100};
    for (int id = 0; id < 3; ++id) {
        std::size_t L = lengths[id];
        for (int c = 0; c < 3; ++c) {
            int K = Ks[c];
            int G = calibrate(id, K);

            for (int trial = 1; trial <= 5; ++trial) {
                int Id = (trial - 1 + id * 3 + c) % 6;
                for (int i = 0; i < 3; ++i) {
                    int mode = perms[Id][i];
                    unsigned long long result = 0;
                    double seconds = time_group(mode, id, K, G, result);
                    csv << "copy," << L << ',' << mode_names[mode] << ",full,"
                        << G << ',' << K << ',' << opt_level << ','
                        << trial << ',' << seconds << ',' << result << '\n';
                }
            }
        }
    }

    csv.close();
}