#include <iostream>
using namespace std;

int cnt = 0;
void toh(int n, string src, string aux, string dest) {
    if (n == 0) return;
    toh(n-1, src, dest, aux);
    cout << cnt << ". move " << src << " to " << dest << endl;
    toh(n-1, aux, src, dest);
}

int main() {
    // Your code here
    toh(3, "A", "B", "C");
    return 0;
}