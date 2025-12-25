#include <iostream>
#include <cstdlib>

int main(int argc, char* argv[]) {
    if (argc < 5) return 1;
    int m = std::atoi(argv[1]);
    int n = std::atoi(argv[2]);
    int a[10][10], b[10][10], c[10][10];
    int k = 0;
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++)
            a[i][j] = std::atoi(argv[3 + k++]);
    k = 0;
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++)
            b[i][j] = std::atoi(argv[3 + n*m + k++]);
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            c[i][j] = a[i][j] + b[i][j];
            std::cout << c[i][j] << " ";
        }
        std::cout << "\n";
    }
    return 0;
}