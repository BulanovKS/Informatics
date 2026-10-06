#ifndef FUNCTIONS_H
#define FUNCTIONS_H

#include <iostream> 
#include <fstream> 
#include <chrono>
#include <random>

// int main()

void slow_sorts(std::string optim);
void quick_sorts();
void quick_sorts_qs();
void small_arrays();


// ВСПОМОГАТЕЛЬНЫЕ ФУНКЦИИ
// Для сортировок

void swap(int & a, int & b);
int find_min(int array[], int start, int n);
void merge(int array [], int l, int mid, int r);
int find_pivot(int array[], int end, int pivot);
void restore_heap(int list[], int listLength, int root);

// Для тестирования

int random_uns(int min, int max);
bool is_sorted(const int array[], int n);
void array_generator(int test_array[], int N, int flag);
double test_sort_from_2_param(void (*func)(int array[], int), int test_array[], int N, int flag, int K);
double test_sort_from_3_param(void (*func)(int array[], int, int), int test_array[], int N, int flag, int K);

// СОРТИРОВКИ
// №0 Медленные сортировки

void bubble_sort(int array[], int n);
void insertion_sort(int array[], int n);
void selection_sort(int array[], int n);

// №1 Быстрые сортировки

void merge_sort(int array[], int l, int r);
void quick_sort(int array[], int l, int r);
void heap_sort(int array[], int n);
void shell_sort(int array[], int n);

#endif