#include "header.h"

std::size_t L = 16384 * 5;

int text_generator() {
    std::ofstream out("text.txt");

    if (out.is_open()) {
        for (std::size_t i = 0; i < L; ++i) {
            for (int s = 0; s < 5; ++s) {
                if (i % 10 == 0) out << ' ';
                else if (i % 15 == 0) out << '\t';
                else out << (char)('a' + ((i + s) % 26));
            }
        }
        out.close();

        std::cout << "Данные успешно записаны в файл." << std::endl;
    } else {
        std::cout << "Не удалось открыть файл для записи." << std::endl;
    }

    return 0;
}