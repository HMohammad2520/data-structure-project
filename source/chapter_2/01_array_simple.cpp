#include <iostream>
#include <cstdlib>

int main(int argc, char* argv[]) {
    if (argc < 2) return 1;

    int n = std::atoi(argv[1]);
    int* a = new int[n];

    for (int i = 0; i < n; i++)
        a[i] = std::atoi(argv[2 + i]);

    for (int i = 0; i < n; i++)
        std::cout << a[i] << " ";
    std::cout << "\n";

    delete[] a;
    return 0;
}