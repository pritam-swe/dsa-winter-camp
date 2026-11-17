#include <iostream>
using namespace std;

int power(int x, int n)
{
    if (n == 0) return 1;
    int smallAns = power(x, n /2);
    int ans;
    if ((n % 2) == 0) {
        ans = smallAns*smallAns;
    } else {
        ans = smallAns*smallAns*n;
    }
    return ans;
}
int main()
{
    // Your code here
    int ans = power(2, 3);
    cout << ans;
    return 0;
}