#pragma once

#include <iostream>

// в структуре по умолчанию все поля открыты, а в контейнере закрыты

class Journal {
private:

    unsigned size_ = 0; // число записанных измерений
    unsigned capacity_ = 0; // количество свободных ячеек
    int* data_ = nullptr;

public:

    Journal(unsigned capacity) { // конструктор - то, что вызывается при создании объекта класса (__init__)
        capacity_ = capacity;
        data_ = new int[capacity];
    }

    Journal(Journal& from) {
        capacity_ = from.capacity_;
        size_ = from.size_;
        data_ = new int[size_ + capacity_];
        for (int i = 0; i < size_; ++i) { data_[i] = from.data_[i]; }
    }

    ~Journal() {
        delete[] data_;
        std::cout << "Deleted elements: " << size_ + capacity_ << "\n";
    }

    Journal& operator=(Journal) = delete; // удаляем оператор присвоения

    bool add(int value) { 
        if (capacity_ <= 0) {
            return false;
        }
        data_[size_] = value;
        capacity_ --;
        size_ ++;
        return true;
    }

    int get(unsigned index) { return data_[index]; }

    int sum() const {
        int result = 0;
        for (int i = 0; i < size_; ++i){
            result += data_[i];
        }
        return result;
    }

    void print_data() const {
        for (int i = 0; i < size_; ++i){
            std::cout << data_[i] << ' ';
        }
        std::cout << "\n";
    }
};