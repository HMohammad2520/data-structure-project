#include <iostream>
#include <cstdlib>

int factorial(int n) {
    if (n == 0) return 1;
    return n * factorial(n - 1);
}

int main(int argc, char* argv[]) {
    if (argc < 2) return 1;
    int n = std::atoi(argv[1]);
    std::cout << factorial(n);
    return 0;
}