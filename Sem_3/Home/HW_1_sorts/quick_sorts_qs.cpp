#include "header.h"

void quick_sorts_qs(){
    std::ofstream f("quick_sorts_qs.csv", std::ios::out); 

    int test_array[100000];
    int test_size[10] = {10, 100, 500, 1000, 5000, 10000, 25000};
    int number_of_iterations[10] = {10, 10, 10, 5, 5, 5, 3};

    f << "Type of array" << "," << "Number" << "," << "Time of quick_sort" << std::endl;

    for (int flag = 0; flag < 3; flag++){
        for (int j = 0; j < 7; j++){

            int N = test_size[j];
            double K = number_of_iterations[j];
            
            double quick_time = test_sort_from_3_param(quick_sort, test_array, N, flag, K);
            std::cout << N << ": Time quick_sort " << quick_time << std::endl;

            f << flag << "," << N << "," << quick_time << std::endl; 
        }
    }
}