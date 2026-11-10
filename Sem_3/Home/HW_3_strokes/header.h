#ifndef FUNCTIONS_H
#define FUNCTIONS_H

#include <cstddef>
#include <string>
#include <chrono>
#include <fstream>
#include <iostream>

//  Оптимизация сборки

const char* opt_level = "O0";

// Структуры

struct Block16 { char data[16]; };
struct Block1024  { char data[1024]; };
struct Block16384 { char data[16384]; };

struct Text {
    const char* data;
    std::size_t size;
};

struct Stats {
    std::size_t words = 0;
    unsigned long long checksum = 0;
};

// Чтение текста из файла

int text_input(const std::string Name, std::string& text);

// Обработчик для Text: короткий и полный

unsigned char first(Text text);
unsigned char first_value(Text text);
unsigned char first_ref(const Text& text);
unsigned char first_ptr(const Text* text);

Stats analyze(Text text);
Stats analyze_value(Text text);
Stats analyze_ref(const Text& text);
Stats analyze_ptr(const Text* text);

// Обработчик для Block16: короткий и полный

unsigned char block16_first_value(Block16 text);
unsigned char block16_first_ref(const Block16& text);
unsigned char block16_first_ptr(const Block16* text);
Stats block16_full_value(Block16 text);
Stats block16_full_ref(const Block16& text);
Stats block16_full_ptr(const Block16* text);

// Обработчик для Block1024: короткий и полный

unsigned char block1024_first_value(Block1024 text);
unsigned char block1024_first_ref(const Block1024& text);
unsigned char block1024_first_ptr(const Block1024* text);
Stats block1024_full_value(Block1024 text);
Stats block1024_full_ref(const Block1024& text);
Stats block1024_full_ptr(const Block1024* text);

// Обработчик для Block16384: короткий и полный

unsigned char block16384_first_value(Block16384 text);
unsigned char block16384_first_ref(const Block16384& text);
unsigned char block16384_first_ptr(const Block16384* text);
Stats block16384_full_value(Block16384 text);
Stats block16384_full_ref(const Block16384& text);
Stats block16384_full_ptr(const Block16384* text);

// Функции от скаляра (для сравнения)

unsigned int scalar_value(unsigned int x);
unsigned int scalar_ref(const unsigned int& x);
unsigned int scalar_ptr(const unsigned int* x);

// Заполнение Block16 / Block1024/ Block16384

void fill_block(char* data, std::size_t size, const std::string& s);

// Функция копирования Text

char* clone_text(Text text);

// Функции заданий

void task_1();
void task_2();
void task_3();

#endif