#include <iostream>
#include <cstdlib>

class Queue {
private:
    int* data;
    int front;
    int rear;
    int capacity;

public:
    Queue(int size) {
        capacity = size;
        data = new int[capacity];
        front = 0;
        rear = -1;
    }

    ~Queue() {
        delete[] data;
    }

    bool isEmpty() {
        return front > rear;
    }

    bool isFull() {
        return rear == capacity - 1;
    }

    void enqueue(int value) {
        if (isFull()) return;
        data[++rear] = value;
    }

    void display() {
        if (isEmpty()) {
            std::cout << "Queue is empty\n";
            return;
        }

        for (int i = front; i <= rear; i++)
            std::cout << data[i] << " ";
        std::cout << "\n";
    }
};

int main(int argc, char* argv[]) {
    if (argc < 2) return 1;

    int n = std::atoi(argv[1]);
    Queue q(n);

    for (int i = 2; i < argc; i++)
        q.enqueue(std::atoi(argv[i]));

    q.display();

    return 0;
}