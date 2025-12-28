#include <iostream>
#include <cstdlib>

using namespace std;

struct Node {
    int data;
    Node* next;
};

class LinkedList {
private:
    Node* head;

public:
    LinkedList() {
        head = NULL;
    }

    void insertEnd(int value) {
        Node* newNode = new Node;
        newNode->data = value;
        newNode->next = NULL;

        if (head == NULL) {
            head = newNode;
            return;
        }

        Node* temp = head;
        while (temp->next != NULL)
            temp = temp->next;

        temp->next = newNode;
    }

    void display() {
        Node* temp = head;
        while (temp != NULL) {
            cout << temp->data << " ";
            temp = temp->next;
        }
        cout << endl;
    }
};

int main(int argc, char* argv[]) {
    if (argc < 2) return 1;

    int n = atoi(argv[1]);
    if (argc < n + 2) return 1;

    LinkedList list;

    for (int i = 0; i < n; i++) {
        int value = atoi(argv[2 + i]);
        list.insertEnd(value);
    }

    list.display();
    return 0;
}
