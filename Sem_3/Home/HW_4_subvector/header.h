#ifndef FUNCTIONS_H
#define FUNCTIONS_H

#include <chrono>
#include <fstream>
#include <iostream>
#include <vector>

// Структура для хранения замеров времени

struct Time {
    double time_sec;
    bool aborted;
};

// Класс subvector

template <typename Type>
class subvector {
public:

    Type* data;
    unsigned int size;
    unsigned int capacity;

    int grow_type;
    double grow_param;
    // grow_type == 0: capacity = capacity + grow_param
    //           == 1: capacity = capacity * grow_param

    subvector();
    ~subvector();

    void set_growth(int type, double param);
    bool push_back(Type d);
    Type pop_back();
    bool resize(unsigned int new_capacity);
    void shrink_to_fit();
    void clear();
};

// Реализация шаблона

template <typename Type>
subvector<Type>::subvector(): data(nullptr), size(0), capacity(0), grow_type(1), grow_param(2.0) {}

template <typename Type>
subvector<Type>::~subvector() {
    delete[] data;
}

template <typename Type>
void subvector<Type>::set_growth(int type, double param) {
    grow_type = type;
    grow_param = param;
}

    // grow_type == 0: capacity = capacity + grow_param
    //           == 1: capacity = capacity * grow_param

template <typename Type>
bool subvector<Type>::push_back(Type d) {
    if (size >= capacity) {
        unsigned int new_cap;
        if (grow_type == 0) {
            new_cap = capacity + static_cast<unsigned int>(grow_param);
        } else {
            new_cap = static_cast<unsigned int>(capacity * grow_param);
        }
        if (new_cap <= capacity) new_cap = capacity + 1;
        if (!resize(new_cap)) return false;
    }
    data[size] = d;
    size++;
    return true;
}

template <typename Type>
Type subvector<Type>::pop_back() {
    if (size == 0) return Type();
    size--;
    return data[size];
}

template <typename Type>
bool subvector<Type>::resize(unsigned int new_capacity) {
    Type* new_data = nullptr;
    if (new_capacity > 0) {
        new_data = new Type[new_capacity];
        unsigned int keep = (size < new_capacity) ? size : new_capacity;
        for (unsigned int i = 0; i < keep; ++i) {
            new_data[i] = data[i];
        }
        delete[] data;
        data = new_data;
        capacity = new_capacity;
        size = keep;
        return true;
    }
    else return false;
    
}

template <typename Type>
void subvector<Type>::shrink_to_fit() {
    if (capacity != size) {
        Type* new_data = nullptr;
        if (size > 0) {
            new_data = new Type[size];
            for (unsigned int i = 0; i < size; ++i) new_data[i] = data[i];
        }
        delete[] data;
        data = new_data;
        capacity = size;
    }
}

template <typename Type>
void subvector<Type>::clear() {
    size = 0;
}

// Вспомогательные функции

double get_time();
Time timed_fill(unsigned int n, int grow_type, double grow_param, double timeout_sec = 20.0);

// Функции заданий

void task0();
void task1();
void task2a();
void task2b();

#endif