#include <iostream>
#include <cstdlib>

int main(int argc, char* argv[]) {
    if (argc < 4) return 1;

    int base = std::atoi(argv[1]);
    int size = std::atoi(argv[2]);
    int i    = std::atoi(argv[3]);

    std::cout << base + i * size << "\n";
    return 0;
}