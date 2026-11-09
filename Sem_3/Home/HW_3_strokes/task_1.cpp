#include "header.h"

void task0() {
    std::cout << "Task 0: Correctness checks\n";

    Text empty{nullptr, 0};
    if (first(empty) != 0) { std::cerr << "FAIL: first empty\n"; return; }
    Stats s = analyze(empty);
    if (s.words != 0 || s.checksum != 0) { std::cerr << "FAIL: analyze empty\n"; return; }

    const char* str = "one two";
    Text t{str, 7};
    if (first(t) != 'o') { std::cerr << "FAIL: first one two\n"; return; }
    s = analyze(t);
    if (s.words != 2 || s.checksum != 700) { std::cerr << "FAIL: analyze one two\n"; return; }

    Text single{"a", 1};
    if (first(single) != 'a') { std::cerr << "FAIL: first single\n"; return; }
    s = analyze(single);
    if (s.words != 1 || s.checksum != 'a') { std::cerr << "FAIL: analyze single\n"; return; }

    Text sep{" \t ", 3};
    if (first(sep) != ' ') { std::cerr << "FAIL: first sep\n"; return; }
    s = analyze(sep);
    if (s.words != 0 || s.checksum != ' ' + '\t' + ' ') { std::cerr << "FAIL: analyze sep\n"; return; }

    Text mixed{"one\ttwo three", 13};
    s = analyze(mixed);
    if (s.words != 3) { std::cerr << "FAIL: analyze mixed\n"; return; }

    std::string long_str(100000, 'a');
    Text long_text{long_str.c_str(), long_str.size()};
    s = analyze(long_text);
    if (s.words != 1 || s.checksum != 100000ULL * 'a') { std::cerr << "FAIL: analyze long\n"; return; }

    char* copy = clone_text(t);
    const char* expected = "one two";
    bool ok = true;
    for (int i = 0; i <= 7; ++i) if (copy[i] != expected[i]) { ok = false; break; }
    if (!ok) { std::cerr << "FAIL: clone_text\n"; delete[] copy; return; }
    delete[] copy;

    char source[] = "one two";
    Text borrowed{source, 7};
    Text descriptor_copy = borrowed;
    char* owned_copy = clone_text(borrowed);
    source[0] = '0';
    if (borrowed.data[0] != '0' || descriptor_copy.data[0] != '0') {
        std::cerr << "FAIL: borrowed sees change\n"; delete[] owned_copy; return;
    }
    if (owned_copy[0] != 'o') {
        std::cerr << "FAIL: owned copy independent\n"; delete[] owned_copy; return;
    }
    delete[] owned_copy;

    Block16 b16;
    fill_block(b16.data, 16, "one two");
    Stats bs_ref = block16_full_ref(b16);
    Stats bs_val = block16_full_value(b16);
    Stats bs_ptr = block16_full_ptr(&b16);
    if (bs_ref.words != bs_val.words || bs_ref.checksum != bs_val.checksum) {
        std::cerr << "FAIL: block value vs ref\n"; return;
    }
    if (bs_ref.words != bs_ptr.words || bs_ref.checksum != bs_ptr.checksum) {
        std::cerr << "FAIL: block ptr vs ref\n"; return;
    }

    Text text_sample{"one two", 7};
    Stats ts_val = analyze_value(text_sample);
    Stats ts_ref = analyze_ref(text_sample);
    Stats ts_ptr = analyze_ptr(&text_sample);
    if (ts_val.words != ts_ref.words || ts_val.checksum != ts_ref.checksum) {
        std::cerr << "FAIL: text value vs ref\n"; return;
    }
    if (ts_val.words != ts_ptr.words || ts_val.checksum != ts_ptr.checksum) {
        std::cerr << "FAIL: text ptr vs ref\n"; return;
    }

    std::cout << "All checks passed.\n";
}