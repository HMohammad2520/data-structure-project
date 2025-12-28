#include <iostream>
#include <cstdlib>

int main(int argc, char* argv[]) {
    if (argc < 4) return 1;

    int r = std::atoi(argv[1]);
    int c = std::atoi(argv[2]);
    int nz = std::atoi(argv[3]);

    int idx = 4;
    for (int i = 0; i < nz; i++) {
        int x = std::atoi(argv[idx++]);
        int y = std::atoi(argv[idx++]);
        int v = std::atoi(argv[idx++]);
        std::cout << x << ":" << y << "=" << v << " ";
    }
    std::cout << "\n";
    return 0;
}