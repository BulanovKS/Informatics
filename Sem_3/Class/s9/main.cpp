#include "container.h"

void function() {
    Journal j(8);
}

int main() {
    Journal tetradka(12);
    for (int i = 0; i < 12; ++i) {
        Journal j(i);
        std::cout << tetradka.add(i) << ' ';
    }
    std::cout << "\n";

    function();

    std::cout << tetradka.sum() << '\n';
    tetradka.print_data();
}