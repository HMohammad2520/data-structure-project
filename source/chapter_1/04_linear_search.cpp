#include <iostream>
#include <cstdlib>

int main(int argc, char* argv[]) {
    if (argc < 3) return 1;
    int n = std::atoi(argv[1]);
    int x = std::atoi(argv[2]);
    int A[100];
    for (int i = 0; i < n; i++)
        A[i] = std::atoi(argv[3 + i]);
    int pos = -1;
    for (int i = 0; i < n; i++)
        if (A[i] == x) {
            pos = i;
            break;
        }
    std::cout << pos << "\n";
    return 0;
}
