#include <iostream>
#include <cstdlib>

int main(int argc, char* argv[]) {
    if (argc < 2) return 1;

    int n = std::atoi(argv[1]);

    for (int i = 1; i <= n; i++) {
        std::cout << i << " ";
    }

    std::cout << "\n";
    return 0;
}