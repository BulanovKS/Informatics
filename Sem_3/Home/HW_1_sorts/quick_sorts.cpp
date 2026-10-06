#include "header.h"

void quick_sorts(){
    std::ofstream f("quick_sorts.csv", std::ios::out); 

    int test_array[100000];
    int test_size[10] = {10, 100, 500, 1000, 5000, 10000, 25000, 50000, 75000, 100000};
    int number_of_iterations[10] = {10, 10, 10, 5, 5, 5, 3, 3, 3, 2};

    f << "Type of array" << "," << "Number" << "," << "Time of merge_sort" << "," << "Time of quick_sort" << "," << "Time of heap_sort" << "," << "Time of shell_sort" << std::endl;

    for (int flag = 0; flag < 3; flag++){
        for (int j = 0; j < 10; j++){

            int N = test_size[j];
            double K = number_of_iterations[j];
            
            double merge_time = test_sort_from_3_param(merge_sort, test_array, N, flag, K);
            std::cout << N << ": Time merge_sort " << merge_time << std::endl;

            double quick_time = test_sort_from_3_param(quick_sort, test_array, N, flag, K);
            std::cout << N << ": Time quick_sort " << quick_time << std::endl;

            double heap_time = test_sort_from_2_param(heap_sort, test_array, N, flag, K);
            std::cout << N << ": Time heap_sort " << heap_time << std::endl;

            double shell_time = test_sort_from_2_param(shell_sort, test_array, N, flag, K);
            std::cout << N << ": Time shell_sort " << shell_time << std::endl;

            f << flag << "," << N << "," << merge_time << "," << quick_time << "," << heap_time << "," << shell_time << std::endl; 
        }
    }
}