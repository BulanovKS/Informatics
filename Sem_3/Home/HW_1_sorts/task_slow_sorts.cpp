#include "header.h"

void task_slow_sorts(){
    std::ofstream f("task_slow_sorts.csv", std::ios::out); 

    int test_array[100000];
    int test_size[10] = {10, 100, 500, 1000, 5000, 10000, 25000, 50000, 75000, 100000};
    int number_of_iterations[10] = {10, 10, 10, 5, 5, 5, 3, 3, 3, 2};

    f << "Type of array" << " | " << "Number" << " | " << "Time of bubble_sort" << " | " << "Time of insertion_sort" << " | " << "Time of selection_sort" << std::endl;

    for (int flag = 0; flag < 3; flag++){
        for (int j = 0; j < 10; j++){

            int N = test_size[j];
            double K = number_of_iterations[j];
            
            double bubble_time = test_sort_from_2_param(bubble_sort, test_array, N, flag, K);
            std::cout << N << ": Time buble_sort " << bubble_time << std::endl;

            double insertion_time = test_sort_from_2_param(insertion_sort, test_array, N, flag, K);
            std::cout << N << ": Time insertion_sort " << insertion_time << std::endl;

            double selection_time = test_sort_from_2_param(selection_sort, test_array, N, flag, K);
            std::cout << N << ": Time selection_sort " << selection_time << std::endl;

            f << flag << " | " << N << " | " << bubble_time << " | " << insertion_time << " | " << selection_time << std::endl; 
        }
    }
}