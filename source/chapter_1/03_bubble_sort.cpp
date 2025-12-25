#include <iostream>
#include <cstdlib>

int main(int argc, char* argv[]) {
    if (argc < 2) return 1;
    int n = std::atoi(argv[1]);
    int A[100];
    for (int i = 0; i < n; i++)
        A[i] = std::atoi(argv[2 + i]);
    for (int i = 0; i < n - 1; i++)
        for (int j = n - 1; j > i; j--)
            if (A[j - 1] > A[j]) {
                int t = A[j];
                A[j] = A[j - 1];
                A[j - 1] = t;
            }
    for (int i = 0; i < n; i++)
        std::cout << A[i] << " ";
    std::cout << "\n";
    return 0;
}