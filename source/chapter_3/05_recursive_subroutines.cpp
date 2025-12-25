#include <iostream>
#include <cstdlib>

int factorial(int n) {
    if (n <= 1) {
        return 1;
    }
    int result = n * factorial(n - 1);

    return result;
}

int main(int argc, char* argv[]) {
    if (argc < 2) {
        std::cerr << "Please provide a number\n";
        return 1;
    }

    int n = std::atoi(argv[1]);
    int fact = factorial(n);
    std::cout << fact << std::endl;

    return 0;
}