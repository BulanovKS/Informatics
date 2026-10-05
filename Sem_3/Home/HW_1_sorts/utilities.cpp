#include "header.hpp"


// ВСПОМОГАТЕЛЬНЫЕ ФУНКЦИИ
// Для сортировок

void swap(int & a, int & b){
    int tmp = a;
    a = b;
    b = tmp;
}

int find_min(int array[], int start, int n){
    int min_ind = start;
    for (int j = start; j < n; j++){
        if (array[j] < array[min_ind]){
            min_ind = j;
        }
    }
    return min_ind;
}

void merge(int array [], int l, int mid, int r){
    int size_1 = mid - l + 1;
    int size_2 = r - mid;

    // Создаем вспомогательные массивы

    int left_array[size_1];
    int right_array[size_2];

    for (int i = 0; i < size_1; i++){
        left_array[i] = array[l + i];
    }
    for (int j = 0; j < size_2; j++){
        right_array[j] = array[mid + j + 1];
    }

    // Сливаем массивы

    int i = 0;
    int j = 0;
    int k = l;

    while (i < size_1 && j < size_2){
        if (left_array[i] < right_array [j]){
            array[k] = left_array[i];
            i++;
        }
        else{
            array[k] = right_array[j];
            j++;
        }
        k++;
    }

    // Переписываем оставшиеся части

    while (i < size_1){
        array[k] = left_array[i];
        i++;
        k++;
    }

    while (j < size_2){
        array[k] = right_array[j];
        j++;
        k++;
    }
}

int find_pivot(int array[], int end, int pivot){
    int i = end;

    // Элементы меньше pivot располагает слева от себя, а больше pivot -- справа 
    // Сам при этом двигается от левого края к "середине"

    while (i > pivot){
        if (array[i] < array[pivot] && i == pivot + 1){
            swap(array[i], array[pivot]);
            pivot++;
        }
        else if (array[i] < array[pivot]){
            swap(array[pivot], array[pivot + 1]);
            swap(array[i], array[pivot]);
            pivot++;
        }
        else{
            i--;
        }    
    }
    return pivot;
}

void restore_heap(int array[], int n, int root){
	int maximal = root;
	int l = 2 * root + 1;
	int r = 2 * root + 2;
	  
	if (l < n && array[l] > array[maximal]){
		maximal = l;
    }
	else if (r < n && array[r] > array[maximal]){
        maximal = r;
    }
	if (maximal != root){
		swap(array[root], array[maximal]);
		restore_heap(array, n, maximal);
	}
}

// Для функций тестирования

bool is_sorted(const int array[], int n){
    for (int i = 0; i < n-1; i++){
        if (array[i+1] < array[i]){
            return false;
        }
    }
    return true;
}

int random_uns(int min, int max){ 
    unsigned seed = std::chrono::steady_clock::now().time_since_epoch().count(); 
    static std::default_random_engine e(seed); 
    std::uniform_int_distribution<int> d(min, max); 
    return d(e);
}

void array_generator(int test_array[], int N, int flag){
    if (flag == 0){
        for (int i = 0; i < N; i++){
            test_array[i] = random_uns(0, 1000000);
        }
    }
    else if (flag == 1){
        for (int i = 0; i < N; i++){
            test_array[i] = i;
        }
    }
    else if (flag == 2){
        for (int i = 0; i < N; i++){
            test_array[i] = N - i;
        }
    }
    else if (flag == 3){
        for (int i = 1; i < N + 1; i++){
            test_array[i] = 50 * i;
        }
    }     
}

// Тестирование сортировок

double test_sort_from_2_param(void (*func)(int array[], int), int test_array[], int N, int flag, int K){
    double result_time;

    for (int k = 0; k < K; k++){
        array_generator(test_array, N, flag);
            
        auto t1=std::chrono::steady_clock::now();
        func(test_array, N);
        auto t2=std::chrono::steady_clock::now();

        result_time += std::chrono::duration<double>(t2-t1).count();
        std::cout << is_sorted(test_array, N) << ' ';
    }
    return result_time / K;
}

double test_sort_from_3_param(void (*func)(int array[], int, int), int test_array[], int N, int flag, int K){
    double result_time;

    for (int k = 0; k < K; k++){
        array_generator(test_array, N, flag);
            
        auto t1=std::chrono::steady_clock::now();
        func(test_array, 0, N - 1);
        auto t2=std::chrono::steady_clock::now();

        result_time += std::chrono::duration<double>(t2-t1).count();
        std::cout << is_sorted(test_array, N) << ' ';
    }
    return result_time / K;
}