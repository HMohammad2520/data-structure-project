#include <iostream>
#include <cstdlib>

struct Node {
    int data;
    Node* next;
};

int main(int argc, char* argv[]) {
    if (argc < 2) return 1;

    int n = std::atoi(argv[1]);
    if (argc < n + 2) return 1;

    Node* head = nullptr;
    Node* tail = nullptr;

    for (int i = 0; i < n; i++) {
        Node* newNode = new Node;
        newNode->data = std::atoi(argv[2 + i]);
        newNode->next = nullptr;

        if (head == nullptr) {
            head = tail = newNode;
        } else {
            tail->next = newNode;
            tail = newNode;
        }
    }

    Node* current = head;
    while (current != nullptr) {
        std::cout << current->data << " ";
        current = current->next;
    }
    std::cout << "\n";

    current = head;
    while (current != nullptr) {
        Node* temp = current;
        current = current->next;
        delete temp;
    }

    return 0;
}