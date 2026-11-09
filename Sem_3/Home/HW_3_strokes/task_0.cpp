#include "header.h"

// Вспомогательные функции для main

int text_input(const std::string Name, std::string& text) {
    std::ifstream input(Name, std::ios::binary);
    if (!input) return 1;
    std::string line;
    while (std::getline(input, line)) {
        if (!line.empty() && line.back() == '\r') line.pop_back();
        for (std::size_t i = 0; i < line.size(); ++i) {
            text[i] = *line.c_str();
        }
        Stats row = analyze({line.c_str(), line.size()});
        std::cout << row.words << ' ' << row.checksum << '\n';
    }
    return input.bad() ? 1 : 0;
}

// Обработчик для Text: короткий

unsigned char first(Text text) { return (text.size == 0 || text.data == nullptr) ? 0 : static_cast<unsigned char>(text.data[0]); }

unsigned char first_value(Text text) { return first(text); }
unsigned char first_ref(const Text& text) { return first(text); }
unsigned char first_ptr(const Text* text) { return first(*text); }

// Обработчик для Text: полный

Stats analyze(Text text) {
    Stats result;
    bool inside_word = false;
    for (std::size_t i = 0; i < text.size; ++i) {
        char c = text.data[i];
        result.checksum += static_cast<unsigned char>(c);
        if (c == ' ' || c == '\t') {
            inside_word = false;
        } 
        else if (!inside_word) {
            ++result.words;
            inside_word = true;
        }
    }
    return result;
}

Stats analyze_value(Text text) { return analyze(text); }
Stats analyze_ref(const Text& text) { return analyze(text); }
Stats analyze_ptr(const Text* text) { return analyze(*text); }

// Обработчик для Block16: короткий и полный

unsigned char block16_first_value(Block16 text) { return static_cast<unsigned char>(text.data[0]); }
unsigned char block16_first_ref(const Block16& text) { return static_cast<unsigned char>(text.data[0]); }
unsigned char block16_first_ptr(const Block16* text) { return static_cast<unsigned char>(text->data[0]); }
Stats block16_full_value(Block16 text) { return analyze({text.data, 15}); }
Stats block16_full_ref(const Block16& text) { return analyze({text.data, 15}); }
Stats block16_full_ptr(const Block16* text) { return analyze({text->data, 15}); }

// Обработчик для Block1024: короткий и полный

unsigned char block1024_first_value(Block1024 text) { return static_cast<unsigned char>(text.data[0]); }
unsigned char block1024_first_ref(const Block1024& text) { return static_cast<unsigned char>(text.data[0]); }
unsigned char block1024_first_ptr(const Block1024* text) { return static_cast<unsigned char>(text->data[0]); }
Stats block1024_full_value(Block1024 text) { return analyze({text.data, 1023}); }
Stats block1024_full_ref(const Block1024& text) { return analyze({text.data, 1023}); }
Stats block1024_full_ptr(const Block1024* text) { return analyze({text->data, 1023}); }

// Обработчик для Block16384: короткий и полный

unsigned char block16384_first_value(Block16384 text) { return static_cast<unsigned char>(text.data[0]); }
unsigned char block16384_first_ref(const Block16384& text) { return static_cast<unsigned char>(text.data[0]); }
unsigned char block16384_first_ptr(const Block16384* text) { return static_cast<unsigned char>(text->data[0]); }
Stats block16384_full_value(Block16384 text) { return analyze({text.data, 16383}); }
Stats block16384_full_ref(const Block16384& text) { return analyze({text.data, 16383}); }
Stats block16384_full_ptr(const Block16384* text) { return analyze({text->data, 16383}); }

// Функции от скаляра (для сравнения)

unsigned int scalar_value(unsigned int x) { return x + 1; }
unsigned int scalar_ref(const unsigned int& x) { return x + 1; }
unsigned int scalar_ptr(const unsigned int* x) { return *x + 1; }

// Заполнение Block16 / Block1024/ Block16384

void fill_block(char* data, std::size_t size, const std::string& s) {
    std::size_t len = s.size();
    if (len > size - 1) len = size - 1;
    for (std::size_t i = 0; i < len; ++i) data[i] = s[i];
    for (std::size_t i = len; i < size - 1; ++i) data[i] = 'a';
    data[size - 1] = '\0';
}

// Функция копирования Text

char* clone_text(Text text) {
    char* copy = new char[text.size + 1];
    for (std::size_t i = 0; i < text.size; ++i) copy[i] = text.data[i];
    copy[text.size] = '\0';
    return copy;
}
