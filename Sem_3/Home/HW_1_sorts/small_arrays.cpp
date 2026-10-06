#include "header.h"

void small_arrays(){
    std::ofstream f("task_small_arrays.csv", std::ios::out); 

    int test_array[1000];
    int test_size[20];
    array_generator(test_size, 20, 3);
    double K = 1000;
    int flag = 0;

    f << "Number" << " | " << "Time of bubble_sort" << " | " << "Time of insertion_sort" << " | " << "Time of selection_sort" << " | " << "Time of merge_sort" << " | " << "Time of quick_sort" << " | " << "Time of heap_sort" << " | " << "Time of shell_sort" << std::endl;

        for (int j = 0; j < 20; j++){

            int N = test_size[j];
            
            double bubble_time = test_sort_from_2_param(bubble_sort, test_array, N, flag, K);
            std::cout << N << ": Time buble_sort " << bubble_time << std::endl;

            double insertion_time = test_sort_from_2_param(insertion_sort, test_array, N, flag, K);
            std::cout << N << ": Time insertion_sort " << insertion_time << std::endl;

            double selection_time = test_sort_from_2_param(selection_sort, test_array, N, flag, K);
            std::cout << N << ": Time selection_sort " << selection_time << std::endl;
            
            double merge_time = test_sort_from_3_param(merge_sort, test_array, N, flag, K);
            std::cout << N << ": Time merge_sort " << merge_time << std::endl;

            double quick_time = test_sort_from_3_param(quick_sort, test_array, N, flag, K);
            std::cout << N << ": Time quick_sort " << quick_time << std::endl;

            double heap_time = test_sort_from_2_param(heap_sort, test_array, N, flag, K);
            std::cout << N << ": Time heap_sort " << heap_time << std::endl;

            double shell_time = test_sort_from_2_param(shell_sort, test_array, N, flag, K);
            std::cout << N << ": Time shell_sort " << shell_time << std::endl;

            f << N << " | " << bubble_time << " | " << insertion_time << " | " << selection_time << " | " << merge_time << " | " << quick_time << " | " << heap_time << " | " << shell_time << std::endl; 
        }
}