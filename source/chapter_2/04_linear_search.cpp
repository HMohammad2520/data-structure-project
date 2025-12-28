#include <iostream>
#include <cstdlib>

int main(int argc, char* argv[]) {
    if (argc < 3) return 1;

    int n = std::atoi(argv[1]);
    int* a = new int[n];

    for (int i = 0; i < n; i++)
        a[i] = std::atoi(argv[2 + i]);

    int key = std::atoi(argv[2 + n]);
    int pos = -1;

    for (int i = 0; i < n; i++)
        if (a[i] == key) { pos = i; break; }

    std::cout << pos << "\n";
    delete[] a;
    return 0;
}