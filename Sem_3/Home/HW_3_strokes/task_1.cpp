#include "header.h"

// Переменные для работы

unsigned int  scalar = 12345;
Block16       b16;
Block1024     b1024;
Block16384    b16384;
Text          text = {nullptr, 0};
std::string   text_storage[3];

const char* mode_names_1[3] = {"value", "ref", "ptr"};
const int   perms_1[6][3] = {{0,1,2},{0,2,1},{1,0,2},{1,2,0},{2,0,1},{2,1,0}};

// Функция измерения времени

double time_measuring(unsigned long long (*fn)(), int repeats, unsigned long long& result) {
    unsigned long long local = 0;
    double total_time = 0;

    for (int i = 0; i < repeats; ++i) {
        auto start = std::chrono::steady_clock::now();
        local += fn();
        auto end = std::chrono::steady_clock::now();
        total_time += std::chrono::duration<double>(end - start).count();
    }
    result = local;
    return total_time;
}

// Функция подбора G - числа повторений

int calibrate(unsigned long long (*fa)(), unsigned long long (*fb)(), unsigned long long (*fc)()) {
    unsigned long long trash = 0;
    
    double ta = time_measuring(fa, 1, trash);
    double tb = time_measuring(fb, 1, trash);
    double tc = time_measuring(fc, 1, trash);

    double max_t = ta;
    if (tb > max_t) max_t = tb;
    if (tc > max_t) max_t = tc;
    if (max_t <= 0.0) return 1;

    int G = (int)(0.1 / max_t);
    if (G < 1) G = 1;
    if (G > 10'000'000) G = 10'000'000;
    return G;
}

// Функция записи результатов в csv

void measure_group(std::ofstream& csv, const char* experiment, std::size_t length, const char* work, unsigned long long (*fa)(), unsigned long long (*fb)(), unsigned long long (*fc)(), int base) {
    int G = calibrate(fa, fb, fc);

    for (int trial = 1; trial <= 5; ++trial) {
        int id = (trial - 1 + base) % 6;

        for (int i = 0; i < 3; ++i) {
            int mode = perms_1[id][i];
            unsigned long long (*fn)() = (mode == 0) ? fa : (mode == 1) ? fb : fc;
            unsigned long long result = 0;

            double seconds = time_measuring(fn, G, result);

            csv << experiment << ',' << length << ',' << mode_names_1[mode] << ','
                << work << ',' << G << ",1," << opt_level << ','
                << trial << ',' << seconds << ',' << result << '\n';
        }
    }
}

void task_1() {

    std::ofstream csv("A_time_" + std::string(opt_level) + ".csv");
    csv.precision(17);
    csv << "experiment,length,mode,work,repeats,uses,opt,trial,seconds,result\n";

    // Скаляр

    measure_group(csv, "scalar", 0, "scalar", []{ return (unsigned long long)scalar_value(scalar); }, []{ return (unsigned long long)scalar_ref(scalar); }, []{ return (unsigned long long)scalar_ptr(&scalar); }, 0);

    // Заполнение Block16 / Block1024/ Block16384

    std::string text_in;
    text_input("text.txt", text_in);

    std::string s; s.reserve(15);
    for (std::size_t i = 0; i < 15; ++i) { s.push_back((char)(text_in[i])); }
    fill_block(b16.data, 16, s);
    
    s.clear(); 
    s.reserve(1023);
    for (std::size_t i = 0; i < 1023; ++i) { s.push_back((char)(text_in[i])); }
    fill_block(b1024.data, 1024, s);
    
    s.clear(); 
    s.reserve(16383);
    for (std::size_t i = 0; i < 16383; ++i) { s.push_back((char)(text_in[i])); }
    fill_block(b16384.data, 16384, s);

    // Измерение времени для блоков Block16 / Block1024/ Block16384 (короткий + полный обработчик)

    measure_group(csv, "Block16", 15, "short", []{ return (unsigned long long)block16_first_value(b16); }, []{ return (unsigned long long)block16_first_ref(b16); }, []{ return (unsigned long long)block16_first_ptr(&b16); }, 1);
    measure_group(csv, "Block16", 15, "full", []{ Stats s = block16_full_value(b16); return (unsigned long long)(s.checksum + s.words); }, []{ Stats s = block16_full_ref(b16);   return (unsigned long long)(s.checksum + s.words); }, []{ Stats s = block16_full_ptr(&b16);  return (unsigned long long)(s.checksum + s.words); }, 2);
    measure_group(csv, "Block1024", 1023, "short", []{ return (unsigned long long)block1024_first_value(b1024); }, []{ return (unsigned long long)block1024_first_ref(b1024); }, []{ return (unsigned long long)block1024_first_ptr(&b1024); }, 3);
    measure_group(csv, "Block1024", 1023, "full", []{ Stats s = block1024_full_value(b1024); return (unsigned long long)(s.checksum + s.words); }, []{ Stats s = block1024_full_ref(b1024);   return (unsigned long long)(s.checksum + s.words); }, []{ Stats s = block1024_full_ptr(&b1024);  return (unsigned long long)(s.checksum + s.words); }, 4);
    measure_group(csv, "Block16384", 16383, "short", []{ return (unsigned long long)block16384_first_value(b16384); }, []{ return (unsigned long long)block16384_first_ref(b16384); }, []{ return (unsigned long long)block16384_first_ptr(&b16384); }, 5);
    measure_group(csv, "Block16384", 16383, "full", []{ Stats s = block16384_full_value(b16384); return (unsigned long long)(s.checksum + s.words); }, []{ Stats s = block16384_full_ref(b16384);   return (unsigned long long)(s.checksum + s.words); }, []{ Stats s = block16384_full_ptr(&b16384);  return (unsigned long long)(s.checksum + s.words); }, 0);

    // Измерение времени Text для разных длин текста

    std::size_t text_lengths_1[3] = {15, 1023, 16383};
    const char* text_names_1[3] = {"Text15", "Text1023", "Text16383"};

    for (int id = 0; id < 3; ++id) {
        std::size_t L = text_lengths_1[id];
        std::string& s = text_storage[id];
        s.reserve(L);
        for (std::size_t i = 0; i < L; ++i) { s.push_back((char)(text_in[i])); }
        text.data = s.c_str();
        text.size = L;

        measure_group(csv, text_names_1[id], L, "short", []{ return (unsigned long long)first_value(text); }, []{ return (unsigned long long)first_ref(text); }, []{ return (unsigned long long)first_ptr(&text); }, id + 1);
        measure_group(csv, text_names_1[id], L, "full", []{ Stats s = analyze_value(text); return (unsigned long long)(s.checksum + s.words); }, []{ Stats s = analyze_ref(text);   return (unsigned long long)(s.checksum + s.words); }, []{ Stats s = analyze_ptr(&text);  return (unsigned long long)(s.checksum + s.words); }, id + 2);
    }

    csv.close();
}