#include <iostream>
#include <cstdlib>

int main(int argc, char* argv[]) {
    if (argc < 3) return 1;

    int r = std::atoi(argv[1]);
    int c = std::atoi(argv[2]);

    int** m = new int*[r];
    for (int i = 0; i < r; i++)
        m[i] = new int[c];

    int idx = 3;
    for (int i = 0; i < r; i++)
        for (int j = 0; j < c; j++)
            m[i][j] = std::atoi(argv[idx++]);

    for (int i = 0; i < r; i++) {
        for (int j = 0; j < c; j++)
            std::cout << &m[i][j] << " ";
        std::cout << "\n";
    }

    for (int i = 0; i < r; i++) delete[] m[i];
    delete[] m;
    return 0;
}