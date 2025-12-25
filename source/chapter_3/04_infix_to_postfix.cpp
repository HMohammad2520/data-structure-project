#include <iostream>
#include <stack>
#include <string>

int precedence(char op) {
    if (op == '+' || op == '-') return 1;
    if (op == '*' || op == '/') return 2;
    return 0;
}

bool isOperator(char c) {
    return c == '+' || c == '-' || c == '*' || c == '/';
}

int main(int argc, char* argv[]) {
    if (argc < 2) {
        std::cout << "No expression provided\n";
        return 1;
    }

    std::string infix = argv[1];
    std::stack<char> st;
    std::string postfix;

    for (char c : infix) {
        if (isalnum(c)) {
            postfix += c; // عملوند → خروجی
        }
        else if (c == '(') {
            st.push(c);
        }
        else if (c == ')') {
            while (!st.empty() && st.top() != '(') {
                postfix += st.top();
                st.pop();
            }
            st.pop(); // حذف '('
        }
        else if (isOperator(c)) {
            while (!st.empty() && precedence(st.top()) >= precedence(c)) {
                postfix += st.top();
                st.pop();
            }
            st.push(c);
        }
    }

    while (!st.empty()) {
        postfix += st.top();
        st.pop();
    }

    std::cout << postfix << std::endl;
    return 0;
}
