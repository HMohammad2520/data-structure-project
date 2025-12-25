#include <iostream>
#include <cstdlib>

int main(int argc, char* argv[]) {
    if (argc < 2) return 1;
    int n = std::atoi(argv[1]);
    int A[100];
    for (int i = 0; i < n; i++)
        A[i] = std::atoi(argv[2 + i]);
    int Max = A[0];
    for (int i = 1; i < n; i++)
        if (A[i] > Max)
            Max = A[i];
    std::cout << Max << "\n";
    return 0;
}