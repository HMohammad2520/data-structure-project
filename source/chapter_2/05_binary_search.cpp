#include <iostream>
#include <cstdlib>

int main(int argc, char* argv[]) {
    if (argc < 3) return 1;

    int n = std::atoi(argv[1]);
    int* a = new int[n];

    for (int i = 0; i < n; i++)
        a[i] = std::atoi(argv[2 + i]);

    int key = std::atoi(argv[2 + n]);

    int l = 0, r = n - 1, mid, res = -1;
    while (l <= r) {
        mid = (l + r) / 2;
        if (a[mid] == key) { res = mid; break; }
        else if (a[mid] < key) l = mid + 1;
        else r = mid - 1;
    }

    std::cout << res << "\n";
    delete[] a;
    return 0;
}