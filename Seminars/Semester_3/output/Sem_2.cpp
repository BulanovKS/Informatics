#include <iostream>

int main(){
    char i;
    int counter = 0;

    do
    {
        std::cin >> i;
        if (i == '1'){
            counter++;
        }
    }while(i == '1' | i == '0');
    std::cout << counter;
}
