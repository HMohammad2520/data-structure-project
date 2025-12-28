#include <iostream>
#include <cstdlib>
#include <string>

#define MAX 100

class Queue {
private:
    int data[MAX];
    int frontIndex, rearIndex;

public:
    Queue() : frontIndex(0), rearIndex(0) {}

    bool isEmpty() const { return frontIndex == rearIndex; }
    bool isFull() const { return rearIndex == MAX; }

    bool enqueue(int value) {
        if (isFull()) return false;
        data[rearIndex++] = value;
        return true;
    }

    bool dequeue(int &removed) {
        if (isEmpty()) return false;
        removed = data[frontIndex++];
        return true;
    }

    bool peek(int &value) const {
        if (isEmpty()) return false;
        value = data[frontIndex];
        return true;
    }
};

int main(int argc, char* argv[]) {
    Queue q;
    for (int i = 1; i < argc; i++) {
        std::string arg = argv[i];

        if (arg == "dequeue") {
            int removed;
            if (q.dequeue(removed))
                std::cout << "DEQUEUE " << removed << std::endl;
            else
                std::cout << "DEQUEUE FAILED" << std::endl;
        }
        else {
            int value = std::atoi(arg.c_str());
            if (q.enqueue(value))
                std::cout << "ENQUEUE " << value << std::endl;
            else
                std::cout << "ENQUEUE FAILED" << std::endl;
        }
    }

    int frontValue;
    if (q.peek(frontValue))
        std::cout << "FRONT " << frontValue << std::endl;
    else
        std::cout << "QUEUE EMPTY" << std::endl;

    return 0;
}