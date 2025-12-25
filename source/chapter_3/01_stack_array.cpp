#include <iostream>
#include <cstdlib>
#include <string>

#define MAX 100

class Stack {
private:
    int data[MAX];
    int top;

public:
    Stack() {
        top = -1;
    }

    bool isEmpty() const {
        return top == -1;
    }

    bool isFull() const {
        return top == MAX - 1;
    }

    bool push(int value) {
        if (isFull())
            return false;
        data[++top] = value;
        return true;
    }

    bool pop(int &removed) {
        if (isEmpty())
            return false;
        removed = data[top--];
        return true;
    }

    // In C++ you can not use `top` as a name in property.
    bool peek(int &value) const {
        if (isEmpty())
            return false;
        value = data[top];
        return true;
    }
};

int main(int argc, char* argv[]) {
    Stack stack;

    for (int i = 1; i < argc; i++) {
        std::string arg = argv[i];

        if (arg == "pop") {
            int removed;
            if (stack.pop(removed))
                std::cout << "POP " << removed << std::endl;
            else
                std::cout << "POP FAILED" << std::endl;
        }
        else {
            int value = std::atoi(arg.c_str());
            if (stack.push(value))
                std::cout << "PUSH " << value << std::endl;
            else
                std::cout << "PUSH FAILED" << std::endl;
        }
    }

    int topValue;
    if (stack.peek(topValue))
        std::cout << "TOP " << topValue << std::endl;
    else
        std::cout << "STACK EMPTY" << std::endl;

    return 0;
}