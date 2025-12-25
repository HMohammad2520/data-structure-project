#include <iostream>
#include <cstdlib>

void Hanoi(int n, char A, char B, char C) {
    if (n == 1) {
        std::cout << "Move disk 1 from " << A << " to " << C << "\n";
        return;
    }
    Hanoi(n - 1, A, C, B);
    std::cout << "Move disk " << n << " from " << A << " to " << C << "\n";
    Hanoi(n - 1, B, A, C);
}

int main(int argc, char* argv[]) {
    if (argc < 2) return 1;
    int n = std::atoi(argv[1]);
    Hanoi(n, 'A', 'B', 'C');
    return 0;
}