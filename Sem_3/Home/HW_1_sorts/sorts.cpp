#include "header.h"

// СОРТИРОВКИ

// №0 Сортировка пузырьком (Bubble sort)

void bubble_sort(int array[], int n){
    for (int i = 0; i < n; i++){
        for (int j = 0; j < n - i - 1; j++){
            if (array[j] > array[j + 1]){
                swap(array[j], array[j + 1]);
            }
        }
    }
}

// №0 Сортировка вставками (Insertion sort)

void insertion_sort(int array[], int n){
    for (int i = 0; i < n - 1; i++){
        int min_ind = i;
        for (int j = i + 1; j < n; j++){
            if (array[j] < array[min_ind]){
                min_ind = j;
            }
        }
        if (min_ind != i){
            swap(array[i], array[min_ind]);
        }
    }
}

// №0 Сортировка выбором (Selection sort)

void selection_sort(int array[], int n){
    for (int i = 0; i < n; i++){
        int ind = find_min(array, i, n);
        swap(array[i], array[ind]);
    }
}

// №1 Сортировка слиянием (Merge sort)

void merge_sort(int array[], int l, int r){

    // Ограничение рекурсии

    if (l < r){
        int mid = (l + r) / int(2);

        merge_sort(array, l, mid);
        merge_sort(array, mid + 1, r);

        merge(array, l, mid, r);
    }
}

// №1 Быстрая сортировка (Quick sort)

void quick_sort(int array[], int l, int r){

    // Ограничение рекурсии

    if (l < r){
        int pivot = find_pivot(array, r, l);

        quick_sort(array, l, pivot - 1);
        quick_sort(array, pivot + 1, r);
    }
}

// №1 Сортировка кучей (Heap sort)

void heap_sort(int array[], int n){

    // Max-куча. Построение кучи

	for(int i = n / 2 - 1; i >= 0; i--){
    	restore_heap(array, n, i);
    }

	// Нахождение максимального элемента, перемещение его из корня в конец массива, балансировка кучи

	for(int i = n - 1; i >= 0; i--){
		swap(array[0], array[i]);
		restore_heap(array, i, 0);
	}
}

// №1 Сортировка Шелла (Shell sort)

void shell_sort(int array[], int n){

    // Уменьшение шага в два раза

	for(int k = n / 2; k > 0; k /= 2){

        // Последовательное прохождение по всем парам, отстоящим друг от друга на k и их сортировка

		for (int i = k; i < n; i++){       
			int j = i;

			while(j >= k && array[j - k] > array[i]){
				swap(array[j], array[j - k]);
				j -= k;
			}
        }
	}
}