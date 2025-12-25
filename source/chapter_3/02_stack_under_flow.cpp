// lessons/stack_underflow.cpp
#include <iostream>
#include <cstdlib>

#define MAX 5

class Stack {
private:
    int data[MAX];
    int top;

public:
    Stack() : top(-1) {}

    bool isEmpty() const {
        return top == -1;
    }

    bool push(int value) {
        if (top == MAX - 1)
            return false;
        data[++top] = value;
        return true;
    }

    bool pop(int &removed) {
        if (isEmpty())
            return false;   // Underflow happens here
        removed = data[top--];
        return true;
    }
};

int main() {
    Stack stack;
    int value;

    // تلاش برای pop بدون هیچ push
    if (!stack.pop(value)) {
        std::cout << "STACK UNDERFLOW" << std::endl;
    }

    return 0;
}
