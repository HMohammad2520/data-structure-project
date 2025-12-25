#include <iostream>
#include <stack>
#include <cstdlib>
#include <string>

int applyOperator(int a, int b, char op) {
    switch (op) {
        case '+': return a + b;
        case '-': return a - b;
        case 'x': return a * b;
        case '/': return a / b;
    }
    return 0;
}

int main(int argc, char* argv[]) {
    std::stack<int> st;

    for (int i = 1; i < argc; i++) {
        std::string token = argv[i];

        // اگر عدد باشد
        if (isdigit(token[0]) || (token[0] == '-' && token.size() > 1)) {
            st.push(std::atoi(token.c_str()));
        }
        // اگر عملگر باشد
        else {
            int b = st.top(); st.pop();
            int a = st.top(); st.pop();
            int result = applyOperator(a, b, token[0]);
            st.push(result);
        }
    }

    std::cout << st.top() << std::endl;
    return 0;
}