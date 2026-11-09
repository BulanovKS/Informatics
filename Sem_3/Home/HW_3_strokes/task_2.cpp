#include "header.h"

struct Variant {
    const char* experiment;
    std::size_t length;
    const char* mode;
    const char* work;
    RunFunc run;
    std::size_t repeats;
};

static Block16    g_b16[10];
static Block1024  g_b1024[10];
static Block16384 g_b16384[10];
static Text       g_t15[10], g_t1023[10], g_t16383[10];
static unsigned int g_scalars[10];

#define DEFINE_SHORT(name, expr) \
    static unsigned long long name(std::size_t repeats) { \
        unsigned long long s = 0; \
        for (std::size_t r = 0; r < repeats; ++r) { s += (expr); } \
        return s; \
    }

#define DEFINE_FULL(name, call) \
    static unsigned long long name(std::size_t repeats) { \
        unsigned long long s = 0; \
        for (std::size_t r = 0; r < repeats; ++r) { \
            Stats st = call; \
            s += st.words * 1000000000ULL + st.checksum; \
        } \
        return s; \
    }

DEFINE_SHORT(run_scalar_value_short, scalar_value(g_scalars[r % 10]))
DEFINE_SHORT(run_scalar_ref_short,   scalar_ref(g_scalars[r % 10]))
DEFINE_SHORT(run_scalar_ptr_short,   scalar_ptr(&g_scalars[r % 10]))

DEFINE_SHORT(run_b16_value_short, block16_first_value(g_b16[r % 10]))
DEFINE_SHORT(run_b16_ref_short,   block16_first_ref(g_b16[r % 10]))
DEFINE_SHORT(run_b16_ptr_short,   block16_first_ptr(&g_b16[r % 10]))
DEFINE_FULL(run_b16_value_full, block16_full_value(g_b16[r % 10]))
DEFINE_FULL(run_b16_ref_full,   block16_full_ref(g_b16[r % 10]))
DEFINE_FULL(run_b16_ptr_full,   block16_full_ptr(&g_b16[r % 10]))

DEFINE_SHORT(run_b1024_value_short, block1024_first_value(g_b1024[r % 10]))
DEFINE_SHORT(run_b1024_ref_short,   block1024_first_ref(g_b1024[r % 10]))
DEFINE_SHORT(run_b1024_ptr_short,   block1024_first_ptr(&g_b1024[r % 10]))
DEFINE_FULL(run_b1024_value_full, block1024_full_value(g_b1024[r % 10]))
DEFINE_FULL(run_b1024_ref_full,   block1024_full_ref(g_b1024[r % 10]))
DEFINE_FULL(run_b1024_ptr_full,   block1024_full_ptr(&g_b1024[r % 10]))

DEFINE_SHORT(run_b16384_value_short, block16384_first_value(g_b16384[r % 10]))
DEFINE_SHORT(run_b16384_ref_short,   block16384_first_ref(g_b16384[r % 10]))
DEFINE_SHORT(run_b16384_ptr_short,   block16384_first_ptr(&g_b16384[r % 10]))
DEFINE_FULL(run_b16384_value_full, block16384_full_value(g_b16384[r % 10]))
DEFINE_FULL(run_b16384_ref_full,   block16384_full_ref(g_b16384[r % 10]))
DEFINE_FULL(run_b16384_ptr_full,   block16384_full_ptr(&g_b16384[r % 10]))

DEFINE_SHORT(run_t15_value_short, first_value(g_t15[r % 10]))
DEFINE_SHORT(run_t15_ref_short,   first_ref(g_t15[r % 10]))
DEFINE_SHORT(run_t15_ptr_short,   first_ptr(&g_t15[r % 10]))
DEFINE_FULL(run_t15_value_full, analyze_value(g_t15[r % 10]))
DEFINE_FULL(run_t15_ref_full,   analyze_ref(g_t15[r % 10]))
DEFINE_FULL(run_t15_ptr_full,   analyze_ptr(&g_t15[r % 10]))

DEFINE_SHORT(run_t1023_value_short, first_value(g_t1023[r % 10]))
DEFINE_SHORT(run_t1023_ref_short,   first_ref(g_t1023[r % 10]))
DEFINE_SHORT(run_t1023_ptr_short,   first_ptr(&g_t1023[r % 10]))
DEFINE_FULL(run_t1023_value_full, analyze_value(g_t1023[r % 10]))
DEFINE_FULL(run_t1023_ref_full,   analyze_ref(g_t1023[r % 10]))
DEFINE_FULL(run_t1023_ptr_full,   analyze_ptr(&g_t1023[r % 10]))

DEFINE_SHORT(run_t16383_value_short, first_value(g_t16383[r % 10]))
DEFINE_SHORT(run_t16383_ref_short,   first_ref(g_t16383[r % 10]))
DEFINE_SHORT(run_t16383_ptr_short,   first_ptr(&g_t16383[r % 10]))
DEFINE_FULL(run_t16383_value_full, analyze_value(g_t16383[r % 10]))
DEFINE_FULL(run_t16383_ref_full,   analyze_ref(g_t16383[r % 10]))
DEFINE_FULL(run_t16383_ptr_full,   analyze_ptr(&g_t16383[r % 10]))

#undef DEFINE_SHORT
#undef DEFINE_FULL

static std::size_t calibrate(RunFunc f) {
    f(1);
    auto start = std::chrono::steady_clock::now();
    f(100);
    auto end = std::chrono::steady_clock::now();
    double elapsed = std::chrono::duration<double>(end - start).count();
    if (elapsed <= 0) return 1000;
    std::size_t r = static_cast<std::size_t>(0.05 / (elapsed / 100.0));
    if (r < 10) r = 10;
    return r;
}

void task1() {
    std::cout << "Task 1: Experiment A\n";
    #ifdef __OPTIMIZE__
        const char* opt = "O2";
    #else
        const char* opt = "O0";
    #endif

    std::ofstream csv("experiment_a.csv");
    if (!csv) { std::cerr << "Failed to open experiment_a.csv\n"; return; }
    csv.precision(17);
    csv << "experiment,length,mode,work,repeats,uses,opt,trial,seconds,result\n";

    for (int i = 0; i < 10; ++i) g_scalars[i] = static_cast<unsigned int>(i + 1);

    std::string s15[10], s1023[10], s16383[10];
    for (int i = 0; i < 10; ++i) {
        s15[i]    = generate_string(15,    static_cast<unsigned>(i));
        s1023[i]  = generate_string(1023,  static_cast<unsigned>(i));
        s16383[i] = generate_string(16383, static_cast<unsigned>(i));
        fill_block(g_b16[i].data,    16,    s15[i]);
        fill_block(g_b1024[i].data,  1024,  s1023[i]);
        fill_block(g_b16384[i].data, 16384, s16383[i]);
        g_t15[i]    = {s15[i].c_str(),    s15[i].size()};
        g_t1023[i]  = {s1023[i].c_str(),  s1023[i].size()};
        g_t16383[i] = {s16383[i].c_str(), s16383[i].size()};
    }

    Variant variants[100];
    std::size_t nv = 0;

    #define ADD(e, l, m, w, f) do { \
        variants[nv].experiment = e; \
        variants[nv].length     = l; \
        variants[nv].mode       = m; \
        variants[nv].work       = w; \
        variants[nv].run        = f; \
        variants[nv].repeats    = calibrate(f); \
        ++nv; \
    } while (0)

    ADD("scalar", 0, "value", "short", run_scalar_value_short);
    ADD("scalar", 0, "ref",   "short", run_scalar_ref_short);
    ADD("scalar", 0, "ptr",   "short", run_scalar_ptr_short);

    ADD("Block16", 15, "value", "short", run_b16_value_short);
    ADD("Block16", 15, "ref",   "short", run_b16_ref_short);
    ADD("Block16", 15, "ptr",   "short", run_b16_ptr_short);
    ADD("Block16", 15, "value", "full",  run_b16_value_full);
    ADD("Block16", 15, "ref",   "full",  run_b16_ref_full);
    ADD("Block16", 15, "ptr",   "full",  run_b16_ptr_full);

    ADD("Block1024", 1023, "value", "short", run_b1024_value_short);
    ADD("Block1024", 1023, "ref",   "short", run_b1024_ref_short);
    ADD("Block1024", 1023, "ptr",   "short", run_b1024_ptr_short);
    ADD("Block1024", 1023, "value", "full",  run_b1024_value_full);
    ADD("Block1024", 1023, "ref",   "full",  run_b1024_ref_full);
    ADD("Block1024", 1023, "ptr",   "full",  run_b1024_ptr_full);

    ADD("Block16384", 16383, "value", "short", run_b16384_value_short);
    ADD("Block16384", 16383, "ref",   "short", run_b16384_ref_short);
    ADD("Block16384", 16383, "ptr",   "short", run_b16384_ptr_short);
    ADD("Block16384", 16383, "value", "full",  run_b16384_value_full);
    ADD("Block16384", 16383, "ref",   "full",  run_b16384_ref_full);
    ADD("Block16384", 16383, "ptr",   "full",  run_b16384_ptr_full);

    ADD("Text15", 15, "value", "short", run_t15_value_short);
    ADD("Text15", 15, "ref",   "short", run_t15_ref_short);
    ADD("Text15", 15, "ptr",   "short", run_t15_ptr_short);
    ADD("Text15", 15, "value", "full",  run_t15_value_full);
    ADD("Text15", 15, "ref",   "full",  run_t15_ref_full);
    ADD("Text15", 15, "ptr",   "full",  run_t15_ptr_full);

    ADD("Text1023", 1023, "value", "short", run_t1023_value_short);
    ADD("Text1023", 1023, "ref",   "short", run_t1023_ref_short);
    ADD("Text1023", 1023, "ptr",   "short", run_t1023_ptr_short);
    ADD("Text1023", 1023, "value", "full",  run_t1023_value_full);
    ADD("Text1023", 1023, "ref",   "full",  run_t1023_ref_full);
    ADD("Text1023", 1023, "ptr",   "full",  run_t1023_ptr_full);

    ADD("Text16383", 16383, "value", "short", run_t16383_value_short);
    ADD("Text16383", 16383, "ref",   "short", run_t16383_ref_short);
    ADD("Text16383", 16383, "ptr",   "short", run_t16383_ptr_short);
    ADD("Text16383", 16383, "value", "full",  run_t16383_value_full);
    ADD("Text16383", 16383, "ref",   "full",  run_t16383_ref_full);
    ADD("Text16383", 16383, "ptr",   "full",  run_t16383_ptr_full);

    #undef ADD

    unsigned long long rng = 12345;
    const int num_trials = 5;
    for (int trial = 1; trial <= num_trials; ++trial) {
        // Fisher-Yates shuffle using LCG
        for (std::size_t i = nv - 1; i > 0; --i) {
            rng = rng * 6364136223846793005ULL + 1442695040888963407ULL;
            std::size_t j = static_cast<std::size_t>((rng >> 33) % (i + 1));
            Variant tmp = variants[i];
            variants[i] = variants[j];
            variants[j] = tmp;
        }
        for (std::size_t i = 0; i < nv; ++i) {
            Variant& v = variants[i];
            auto t1 = std::chrono::steady_clock::now();
            unsigned long long sum = v.run(v.repeats);
            auto t2 = std::chrono::steady_clock::now();
            double sec = std::chrono::duration<double>(t2 - t1).count();
            csv << v.experiment << ',' << v.length << ',' << v.mode << ',' << v.work << ','
                << v.repeats << ",1," << opt << ',' << trial << ',' << sec << ',' << sum << '\n';
        }
    }

    csv.close();
    std::cout << "Experiment A completed. Results saved to experiment_a.csv\n";
}