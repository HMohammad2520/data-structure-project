#include <iostream>
#include <cstdlib>

int fib(int n) {
    if (n == 1) return 0;
    if (n == 2) return 1;
    return fib(n - 1) + fib(n - 2);
}

int main(int argc, char* argv[]) {
    if (argc < 2) return 1;
    int n = std::atoi(argv[1]);
    std::cout << fib(n) << "\n";
    return 0;
}